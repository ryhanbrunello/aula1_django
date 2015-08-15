# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoa.models import Pessoa

def index(request):
    pessoas = Pessoa.objects.all().order_by('nome')

    #pessoas = Pessoa.objects.raw('select a.id, a.nome, a.idade, b.telefone from pessoa_pessoa a, pessoa_telefone b where a.id = b.pessoa_id')

    #pessoas = Pessoa.objects.raw('select a.id, a.nome, a.idade from pessoa_pessoa a where a.id = 1')

    return render(request, 'index.html', {'msg': u'É isso ai Ryhan!', 'pessoas':pessoas})