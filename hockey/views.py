from urllib.request import Request, urlopen
from django.shortcuts import render,redirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from django.contrib.auth.decorators import login_required
#incluyendo librerias para consumir servicios web.
import json

def index(request):
    listaArticulos = Articulo.objects.all()
    paginator = Paginator(listaArticulos, 3)
    page = request.GET.get('page')
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'articulos':articulos,})

@login_required(login_url='index')
def sumarVotosArticulo(request, id_articulo):
    articulo = Articulo.objects.get(pk=id_articulo)
    articulo.votos = articulo.votos + 1
    articulo.save()
    return redirect('index')

@login_required(login_url='index')
def restarVotosArticulo(request, id_articulo):
    articulo = Articulo.objects.get(pk=id_articulo)
    articulo.votos = articulo.votos - 1
    articulo.save()
    return redirect('index')

@login_required
def addArticulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticuloForm
        return render(request,'newArticulo.html',{'form':form})

def addComentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArticuloForm
        return render(request,'newComentario.html',{'form':form})

def articulo(request,id_articulo):
    articulo = Articulo.objects.get(pk=id_articulo)
    comentarios = Comentario.objects.filter(articulo=id_articulo)
    return render(request,'articulo.html',{'articulo':articulo, 'comentarios':comentarios})

def consumoPersonas(request):
    peticion = Request('http://localhost:8000/api/links/listaPersonas/')

    data_json = []

    try:
        response = urlopen(peticion)
        data_raw = response.read()
        data_json = json.loads(data_raw)
    except:
        print('error')

    listaNombre = []

    for data in data_json:
        name = str(data['nombre'])
        listaNombre.append(name)
    return HttpResponse(listaNombre)
