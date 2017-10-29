# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import permission_required, login_required

# from django.template import RequestContext

from .forms import CadastroUsuarioForm


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


@permission_required()
def VagaListView(request):
    return render(request, 'empresa.html')


@permission_required()
def candidato(request):
    return render(request, 'candidato.html')
