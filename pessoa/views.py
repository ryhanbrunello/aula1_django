# coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from pessoa.models import Pessoa
from pessoa.forms import PessoaFormulario
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

# API
from pessoa.api import PessoaApi
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
import rest_framework_filters as filtro
from rest_framework.permissions import IsAdminUser

class Filtro_Pessoa(filtro.FilterSet):
    nome = filtro.AllLookupsFilter(name='nome')
    class Meta:
        model = Pessoa
        fields = ['nome']

class Api_Automatica(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaApi
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('nome')
    filter_class = Filtro_Pessoa
    permission_classes = (IsAdminUser,)
    paginate_by = 3

@api_view(['POST','GET'])
def api_manual(request):
    if request.method == 'POST':
        if request.POST.get('id',None):
            try:
                pessoa = Pessoa.objects.get(pk=request.POST['id'])
            except:
                return Response("{ msg: 'Id Invalido' }", status=status.HTTP_400_BAD_REQUEST)
        else:
            pessoa = Pessoa()

        pessoaApi = PessoaApi(pessoa, data=request.data, partial=True)

        if pessoaApi.is_valid():
            pessoaApi.save()
            return Response(pessoaApi.data, status=status.HTTP_200_OK)
        else:
            return Response(pessoaApi.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        pessoas = Pessoa.objects.all()
        pessoaApi = PessoaApi(pessoas, many=True)
        return Response(pessoaApi.data)
# FIM API




# =====================================================================================================================
def index(request):
    pessoas = Pessoa.objects.all()
    msg = _(u"Isso é uma vergonha")
    return render(request,'conteudo.html',{'msg':msg, 'pessoas':pessoas})

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

            messages.info(request, _(u'Pessoa inserida com sucesso'))
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