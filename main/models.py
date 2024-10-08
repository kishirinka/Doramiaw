import uuid
from django.db import models
from django.contrib.auth.models import User

class ObjectEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()