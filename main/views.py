from django.shortcuts import render

def show_main(request):
    context = {
        "nama_aplikasi" : "Doramiaw",
        "nama" : "Irma Nia Alwijah",
        "kelas" : "PBP B",
    }

    return render(request, "main.html", context)