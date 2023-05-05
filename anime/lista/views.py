from django.shortcuts import get_object_or_404, render,loader,redirect
from django.http import HttpResponse
from .models import Anime
from .forms import AnimeForm

from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def pendientes(request):
    animes_pendientes = Anime.objects.filter(visto=False)
    animes_pendientes = Anime.objects.order_by('nombre')
    return render(request, 'pendiente.html', {'animes': animes_pendientes})

def vistos(request):
    animes_vistos = Anime.objects.filter(visto=True)
    animes_vistos = Anime.objects.order_by('nombre')
    return render(request, 'vistos.html', {'animes': animes_vistos})


def form(request):
    return render(request,'form.html')


# def guardar_anime(request):
#     if request.method == 'POST':
#         form = AnimeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lista:vistos')
#     else:
#         form = AnimeForm()

#     return render(request, 'form.html', {'form': form})
def guardar_anime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            anime = form.save(commit=False)
            anime.visto = request.GET.get('pagina') == 'vistos'
            anime.save()
            if request.GET.get('pagina') == 'vistos':
                return redirect('lista:vistos')
            else:
                return redirect('lista:pendiente')
    else:
        form = AnimeForm()

    return render(request, 'form.html', {'form': form})






def eliminar_anime(request, tarjeta_id, vista):
    tarjeta = get_object_or_404(Anime, id=tarjeta_id)
    tarjeta.delete()
    if vista == 'pendiente':
        return redirect('lista:pendiente')
    elif vista == 'vistos':
        return redirect('lista:vistos')


def editar_anime(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    anime.visto = True
    anime.save()
    return redirect('lista:vistos')


def modificar_anime(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        url = request.POST.get('imagen')
        anime.nombre = nombre
        anime.imagen = url
        anime.save()
        return redirect('lista:vistos')
    else:
        return render(request, 'modificar_anime.html', {'tarjeta': anime})
