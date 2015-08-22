# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoa.models import Pessoa
from pessoa.forms import PessoaFormulario
from django.contrib import messages

def index(request):
    return render(request,'conteudo.html')

def inserir(request):
    if request.method == "POST":

        pessoa = Pessoa(
            id = request.POST.get('id') if request.POST.get('id',None) else None,
            nome = request.POST.get('nome'),
            idade = request.POST.get('idade'))

        pessoa.save()

    return HttpResponseRedirect('/')

def inserirForm(request):
    if request.method == "POST":
        form  = PessoaFormulario(request.POST)

        if form.is_valid():
            dados = form.cleaned_data
            print dados

            request.session['sessao_nome'] = dados['nome'].upper()

            messages.info(request, 'Pessoa inserida com sucesso')
            messages.success(request, 'Mais um teste!')
            form.save()

    return render(request,'index.html',{'form':form})

def excluir(request, codigo):
    pessoa = Pessoa.objects.get(pk=codigo)
    pessoa.delete()

    return HttpResponseRedirect('/')

def pesquisar(request):
    if request.method == "GET":
        #pessoas = Pessoa.objects.filter(nome__icontains=request.GET.get('busca'))
        #pessoas = Pessoa.objects.raw(select * from pessoa_pessoa)

        selecao = {}#dicionario

        if request.GET.get('busca'):
            selecao['nome__icontains'] = request.GET.get('busca')

        selecao['idade__gt'] = 0

        pessoas = Pessoa.objects.filter(**selecao).order_by('-nome')#traço no order_by é igual a desc

    return render(request,'index.html', {'msg':'Resultado da Busca', 'pessoas':pessoas})

def editar(request, codigo):
    try:
        pessoa = Pessoa.objects.get(pk=codigo)
        return render(request,'index.html', {'pessoa':pessoa})

    except Exception, e:
        return HttpResponseRedirect('/')