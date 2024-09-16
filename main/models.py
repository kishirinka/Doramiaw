import uuid
from django.db import models

class ObjectEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=100)
    description = models.TextField()