# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoa.models import Pessoa

def index(request):
    pessoas = Pessoa.objects.all()

    return render(request, 'index.html', {'msg': u'É isso ai Ryhan!', 'pessoas':pessoas})