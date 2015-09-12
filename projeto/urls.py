"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

#API
from rest_framework import routers
from pessoa import views

rota = routers.DefaultRouter()
rota.register(r'pessoa',views.Api_Automatica, 'Pessoa')
#FIM API


urlpatterns = [
    url(r'^$', 'core.views.index'),
    url(r'^caminho/link1/$','core.views.link1', name='link1'),
    url(r'^caminho/link2/$','core.views.link2', name='link2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pessoa/',include("pessoa.urls")),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^api/', include(rota.urls)),
    url(r'^api_manual/$', 'pessoa.views.api_manual'),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^consulta/api/$', 'pessoa.views.consulta_api'),
    url(r'^incluir/api/$', 'pessoa.views.incluir_api'),
    url(r'^excluir/api/$', 'pessoa.views.excluir_api'),
    url(r'^editar/api/$', 'pessoa.views.editar_api'),
]
