from django.shortcuts import render, HttpResponseRedirect
from pessoa.models import Pessoa

def inserir(request):
    if request.method == "POST":

        pessoa = Pessoa(
            id = request.POST.get('id') if request.POST.get('id',None) else None,
            nome = request.POST.get('nome'),
            idade = request.POST.get('idade'))

        pessoa.save()

    return HttpResponseRedirect('/')

def excluir(request, codigo):
    pessoa = Pessoa.objects.get(pk=codigo)
    pessoa.delete()

    return HttpResponseRedirect('/')

def pesquisar(request):
    if request.method == "GET":
        pessoas = Pessoa.objects.filter(nome__contains=request.GET.get('busca'))

    return render(request,'index.html', {'msg':'Resultado da Busca', 'pessoas':pessoas})

def editar(request, codigo):
    try:
        pessoa = Pessoa.objects.get(pk=codigo)
        return render(request,'index.html', {'pessoa':pessoa})

    except Exception, e:
        return HttpResponseRedirect('/')
    

    