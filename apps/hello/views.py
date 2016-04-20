from django.shortcuts import render_to_response
from apps.hello.models import *


def index(request):
    if Persons.objects.filter(id=1):
        person = Persons.objects.get(id=1)
    else:
        person = False
    return render_to_response('hello/index.html', {'person': person})
