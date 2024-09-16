from django.forms import ModelForm
from main.models import ObjectEntry

class ObjectEntryForm(ModelForm):
    class Meta:
        model = ObjectEntry
        fields = ["name", "price", "category", "description"]