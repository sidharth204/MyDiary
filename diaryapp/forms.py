from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import DiaryEntry


class DiaryEntryForm(forms.ModelForm):

    class Meta:
        model = DiaryEntry

        fields = [
            'title',
            'category',
            'mood',
            'is_pinned',
            'content'
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Give your entry a title...'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'mood': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'is_pinned': forms.CheckboxInput(
                attrs={
                    'class': 'checkbox-input'
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'form-control textarea',
                    'placeholder': 'Write your thoughts here...'
                }
            ),
        }


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }
        )
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Choose a username'
                }
            ),
        }