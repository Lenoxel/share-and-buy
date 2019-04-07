from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def planos(request):
    return render(request, 'planos.html')

def suporte(request):
    return render(request, 'suporte.html')

def afiliado(request):
    return render(request, 'afiliado.html')

def produtor(request):
    return render(request, 'produtor.html')
