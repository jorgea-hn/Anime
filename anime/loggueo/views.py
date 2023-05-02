from django.shortcuts import render,loader
from django.http import HttpResponse


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())
