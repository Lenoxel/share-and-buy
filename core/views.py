from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'index.html')

def planos(request):
    return render(request, 'index.html')

def suporte(request):
    return render(request, 'index.html')

