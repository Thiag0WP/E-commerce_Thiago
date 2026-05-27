from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def teste(request):
    return HttpResponse("Teste de rota para produtos")