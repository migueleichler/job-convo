"""job_convo URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from core import views as core_views

url_home = [
    url(r'^$', core_views.home, name='home'),
    url(r'^vagas/$', login_required(core_views.VagaListView.as_view()),
        name='vagas'),
    url(r'^vaga/(?P<pk>\d+)$', core_views.VagaDetailView.as_view(),
        name='vaga'),
    url(r'^vaga/new/$', core_views.VagaCreate.as_view(),
        name='vaga_new'),
    url(r'^edit/(?P<pk>\d+)$', core_views.VagaUpdate.as_view(),
        name='vaga_edit'),
    url(r'^delete/(?P<pk>\d+)$', core_views.VagaDelete.as_view(),
        name='vaga_delete'),
    url(r'^perfil/new/$', core_views.PerfilCandidatoCreate.as_view(),
        name='perfil_new'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core_views.index, name='index'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^cadastro/', core_views.cadastro, name='cadastro'),
    url(r'^home/', include(url_home), name='home'),
]
