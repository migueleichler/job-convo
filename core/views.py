# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required

from .forms import CadastroUsuarioForm
from core.models import Vaga, PerfilCandidato, Candidatura


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cadastro.html', {'form': form})


@login_required(login_url='/login/')
def home(request):
    group = request.user.groups.filter(user=request.user)[0]
    if group.name == "empresa":
        return HttpResponseRedirect(reverse('empresa'))
    elif group.name == "candidato":
        return HttpResponseRedirect(reverse('candidato'))

    return render(request)


def candidato(request):
    return render(request, "home.html")


def empresa(request):
    return render(request, "home.html")


@permission_required('core.add_candidatura')
def CandidaturaVagaCreate(request, id):
    data = dict()
    if request.method == 'GET':
        candidato_id = request.user.id
        candidatura, created = Candidatura.objects.get_or_create(
                                   candidato_id=candidato_id,
                                   vaga_id=id
                               )
        if created:
            data['response'] = 'Candidatura Confirmada.'
        else:
            data['response'] = 'Candidatura já realizada.'
    return JsonResponse(data)


class VagaList(ListView):
    model = Vaga
    context_object_name = 'vagas'
    template_name = 'vagas.html'

    def get_queryset(self):
        queryset = Vaga.objects.all()
        if self.request.user.has_perm('core.add_vaga'):
            queryset = queryset.filter(empresa=self.request.user)

        return queryset


class VagaDetail(DetailView):
    model = Vaga
    template_name = 'vaga.html'

    def get_context_data(self, **kwargs):
        context = super(VagaDetail, self).get_context_data(**kwargs)
        vaga = self.object
        candidatos = PerfilCandidato.objects.filter(
                        pretensao__gte=vaga.pretensao_minima,
                        pretensao__lte=vaga.pretensao_maxima
                     )
        context['candidatos'] = candidatos.filter(
                                  experiencia=vaga.experiencia,
                                  escolaridade=vaga.escolaridade,
                                  distancia=vaga.distancia
                                )
        perfil = len(context['candidatos'])
        total = PerfilCandidato.objects.all().count()
        context['candidatos_perfil'] = len(context['candidatos'])
        context['candidatos_fora_perfil'] = total - perfil
        return context


class VagaCreate(CreateView):
    model = Vaga
    success_url = reverse_lazy('home')
    template_name = 'vaga_new.html'
    fields = ('nome', 'pretensao_minima', 'pretensao_maxima',
              'experiencia', 'escolaridade', 'distancia',)

    def form_valid(self, form):
        user = self.request.user
        form.instance.empresa = user
        return super(VagaCreate, self).form_valid(form)


class VagaUpdate(UpdateView):
    model = Vaga
    success_url = reverse_lazy('home')
    template_name = 'vaga_update.html'
    fields = ('nome', 'pretensao_minima', 'pretensao_maxima',
              'experiencia', 'escolaridade', 'distancia',)


class VagaDelete(DeleteView):
    model = Vaga

    def delete(self, request, *args, **kwargs):
        data = dict()
        self.object = super(VagaDelete, self).get_object()
        self.object.delete()
        vagas = Vaga.objects.filter(empresa=self.request.user)
        data['html_vagas'] = render_to_string('partial-vagas-empresa.html', {
            'vagas': vagas
        })
        return JsonResponse(data)


class PerfilCandidatoCreate(CreateView):
    model = PerfilCandidato
    success_url = reverse_lazy('home')
    template_name = 'perfil_candidato_new.html'
    fields = ('pretensao', 'experiencia',
              'escolaridade', 'distancia',)

    def form_valid(self, form):
        user = self.request.user
        form.instance.candidato = user
        return super(PerfilCandidatoCreate, self).form_valid(form)


class CandidaturaList(ListView):
    model = Vaga
    context_object_name = 'vagas'
    template_name = 'candidaturas.html'

    def get_queryset(self):
        user = self.request.user
        vagas = Candidatura.objects.filter(candidato=user).values('vaga')
        queryset = Vaga.objects.filter(id__in=vagas)

        return queryset
