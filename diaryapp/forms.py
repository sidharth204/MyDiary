from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import DiaryEntry


class DiaryEntryForm(forms.ModelForm):

    class Meta:
        model = DiaryEntry
        fields = ['title', 'content']


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']