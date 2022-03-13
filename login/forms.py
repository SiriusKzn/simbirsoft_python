from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Электронная почта:", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Введите e-mail',
                                                                                       'id': "exampleInputEmail1"}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повторите пароль:',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Введите пароль'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'id': 'inputEmail3',
                                                           'placeholder': 'Введите эл. почту'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'id': 'inputPassword3',
                                                                 'placeholder': 'Введите пароль'}))
