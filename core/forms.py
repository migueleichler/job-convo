# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import UserCreationForm


class CadastroUsuarioForm(UserCreationForm):
    tipo = forms.ChoiceField(choices=(
        (1, ('Empresa')),
        (2, ('Candidato')),
    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'tipo',)

    def clean_password(self):
        password = self.cleaned_data.get("password1")
        return password

    def save(self, commit=True):
        user = super(CadastroUsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        if self.cleaned_data['tipo'] == '1':
            grupo = Group.objects.get(name='empresa')
        else:
            grupo = Group.objects.get(name='candidato')
        grupo.user_set.add(user)
        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        labels = {
            'username': 'Usuário',
            'password': 'Senha',
        }
