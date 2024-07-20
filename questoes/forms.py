from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Questao
from ckeditor.widgets import CKEditorWidget

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ['enunciado', 'disciplina', 'gabarito']
        widgets = {
            'enunciado': CKEditorWidget(),
        }

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
