from django.conf.urls import url
from django.contrib.auth import views as auth_views

from core import views as core_views


url_empresa = [
    url(r'^$', core_views.empresa, name='empresa'),
    url(r'^vagas/$', core_views.VagaListView.as_view(),
        name='vagas'),
    url(r'^vaga/(?P<pk>\d+)$', core_views.VagaDetailView.as_view(),
        name='vaga'),
    url(r'^vaga/new/$', core_views.VagaCreate.as_view(),
        name='vaga_new'),
    url(r'^vaga/edit/(?P<pk>\d+)$', core_views.VagaUpdate.as_view(),
        name='vaga_edit'),
    url(r'^vaga/delete/(?P<pk>\d+)$', core_views.VagaDelete.as_view(),
        name='vaga_delete'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]


url_candidato = [
    url(r'^$', core_views.candidato, name='candidato'),
    url(r'^perfil/new/$', core_views.PerfilCandidatoCreate.as_view(),
        name='perfil_new'),
    url(r'^candidatura/$', core_views.VagaListView.as_view(),
        name='vagas'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
