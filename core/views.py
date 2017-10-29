# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import permission_required, login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import CadastroUsuarioForm
from .models import models as core_models


def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/home/')
    else:
        form = CadastroUsuarioForm()
    return render(request, 'cadastro.html', {'form': form})


@login_required(login_url='/login/')
def home(request):
    # if request.user.has_perm('pode_criar_vaga'):
    #     return redirect('/empresa/')
    # else:
    #     return redirect('/candidato/')

    # if request.user.groups.filter(name='empresa').exists():
    #     return redirect('/empresa/')
    # else:
    #     return redirect('/candidato/')
    return render(request, 'home.html')


# @permission_required('can_vaga')
class VagaListView(generic.ListView):
    model = core_models.Vaga
    context_object_name = 'vaga_list'
    template_name = 'candidato.html'


class VagaDetailView(generic.DetailView):
    model = core_models.Vaga
    template_name = 'candidato.html'


class VagaCreate(CreateView):
    model = core_models.Vaga
    success_url = reverse_lazy('server_list')
    fields = ('empresa', 'nome', 'perfil',)


class VagaUpdate(UpdateView):
    model = core_models.Vaga
    success_url = reverse_lazy('server_list')
    fields = ('empresa', 'nome', 'perfil',)


class VagaDelete(DeleteView):
    model = core_models.Vaga
    success_url = reverse_lazy('server_list')
