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

from core import views as core_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', core_views.index, name='index'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^cadastro/', core_views.cadastro, name='cadastro'),
    # url(r'^curriculos/$', core_views.CurriculoListView.as_view(), name='curriculos'),
    # url(r'^curriculo/$', core_views.curriculo, name='curriculo'),
    # url(r'^vagas/$', core_views.VagaListView.as_view(), name='vagas'),
    # url(r'^vaga/(?P<pk>\d+)$', core_views.cadastro, name='vaga'),
]
