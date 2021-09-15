from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def novo_servico(request):
    return render(request, 'novo_servico.html')
