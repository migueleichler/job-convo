from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import permission_required

from core import views as core_views


url_empresa = [
    url(r'^$', core_views.empresa, name='empresa'),
    url(r'^vagas/$',
        permission_required('core.add_vaga')(core_views.VagaList.as_view()),
        name='vagas'),
    url(r'^vaga/(?P<pk>\d+)$',
        permission_required('core.add_vaga')(core_views.VagaDetail.as_view()),
        name='vaga'),
    url(r'^vaga/new/$',
        permission_required('core.add_vaga')(core_views.VagaCreate.as_view()),
        name='vaga_new'),
    url(r'^vaga/edit/(?P<pk>\d+)$',
        permission_required('core.add_vaga')(core_views.VagaUpdate.as_view()),
        name='vaga_edit'),
    url(r'^vaga/delete/(?P<pk>\d+)$',
        permission_required('core.add_vaga')(core_views.VagaDelete.as_view()),
        name='vaga_delete'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]


url_candidato = [
    url(r'^$', core_views.candidato, name='candidato'),
    url(r'^perfil/new/$',
        permission_required('core.add_candidatura')(core_views.PerfilCandidatoCreate.as_view()),
        name='perfil_new'),
    url(r'^vagas/$',
        permission_required('core.add_candidatura')(core_views.VagaList.as_view()),
        name='vagas'),
    url(r'^candidaturas/$',
        permission_required('core.add_candidatura')(core_views.CandidaturaList.as_view()),
        name='candidaturas'),
    url(r'^candidatura/vaga/(?P<id>\d+)$', core_views.CandidaturaVagaCreate,
        name='candidatura_vaga'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
