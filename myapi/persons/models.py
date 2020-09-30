from django.db import models
import uuid

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    vector = models.CharField(max_length=10000000, blank=True)

    def __str__(self):
        return self.name + " " + self.surname