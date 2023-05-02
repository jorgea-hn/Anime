from django.shortcuts import render,loader
from django.http import HttpResponse
from .models import Anime

# Create your views here.
def pendientes(request):
    # pendientes = Anime.objects.filter(estado=False) # Filtra los animes por ver
    # return render(request, 'pendientes.html', {'pendientes': pendientes})
    return render(request, 'pendiente.html')

def vistos(request):
    # vistos = Anime.objects.filter(estado=True) # Filtra los animes vistos
    # return render(request, 'vistos.html', {'vistos': vistos})
    return render(request, 'vistos.html')

def form(request):
    
    return render(request,'form.html')