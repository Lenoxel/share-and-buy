from django.shortcuts import render

def teste(request):
    return render(request, 'teste.html', {})

def index(request):
    return render(request, 'index.html', {})

