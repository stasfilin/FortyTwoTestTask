from django.contrib import admin
from apps.hello.models import *


class PersonsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date', 'email')

admin.site.register(Persons, PersonsAdmin)