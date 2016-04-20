from django.db import models

__all__ = ('Persons',)


class Persons(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date = models.DateField()
    bio = models.TextField(max_length=512)
    email = models.EmailField(max_length=50)
    jabber = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    other = models.TextField(max_length=512)