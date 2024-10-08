from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse
from main.forms import ObjectEntryForm
from main.models import ObjectEntry
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
from django.http import  HttpResponseRedirect
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_main(request):
    if request.user.is_authenticated:
        
        context = {
            "nama_aplikasi": "Doramiaw",
            "nama": request.user.username,
            "kelas": "PBP B",
            'last_login': request.COOKIES.get('last_login'),
        }

        return render(request, "main.html", context)
    
    # Jika belum login, arahkan ke welcome.html
    return render(request, 'welcome.html')

def show_welcome(request):
    return render(request, 'welcome.html')


def create_object_entry(request):
    form = ObjectEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        object_entry = form.save(commit=False)
        object_entry.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_object_entry.html", context)

def show_xml(request):
    data = ObjectEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = ObjectEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ObjectEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ObjectEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:welcome'))
    response = HttpResponseRedirect(reverse('main:welcome'))
    response.delete_cookie('last_login')
    return response

def edit_object(request, id):
    # Get mood entry berdasarkan id
    object = ObjectEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ObjectEntryForm(request.POST or None, instance=object)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_object.html", context)

def delete_object(request, id):
    # Get mood berdasarkan id
    object = ObjectEntry.objects.get(pk = id)
    # Hapus mood
    object.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_object_entry_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    category = request.POST.get("category")
    description = request.POST.get("description")
    user = request.user

    new_object = ObjectEntry(
        name=name, price=price,
        category=category,
        description=description,
        user=user,
    )
    new_object.save()

    return HttpResponse(b"CREATED", status=201)
