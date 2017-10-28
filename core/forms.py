# -*- coding: utf-8 -*-
from django import forms
# from django.core.exceptions import ValidationError

from .models import UsuarioPadrao


class CadastroUsuarioForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=(
        (1, ('Empresa')),
        (2, ('Cliente')),
    ))

    class Meta:
        model = UsuarioPadrao
        fields = ('username', 'email', 'password', 'tipo',)
        labels = {
            'email': 'Email',
            'password': 'Senha',
            'tipo': 'Tipo de Usuário',
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True):
        user = super(CadastroUsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = UsuarioPadrao
        fields = ('username', 'email', 'password',)
        labels = {
            'email': 'Email',
            'password': 'Senha',
        }
