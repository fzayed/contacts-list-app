from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    email = models.EmailField(max_length=300)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.name
