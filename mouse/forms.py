from django.contrib.auth.models import User
from django import forms
from .models import Block
from django.contrib.auth.forms import UserCreationForm


class AddBlock(forms.ModelForm):
    msg = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Message', 'data-role': "input"}))
    nonce = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nonce', 'data-role': "input", 'class': 'mt-2 mb-2'}))

    class Meta:
        model = Block
        fields = (
            'msg',
            'nonce'
        )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        error_messages={'required': 'Это поле обязательно.'}
    )
    email = forms.EmailField(max_length=254, required=True,
                             error_messages={
                                 'max_length': 'Максимальная' +
                                               'длина почты - 254.',
                                 'required':
                                     'Это поле обязательно.'})

    error_messages = {
        'required': 'Это поле обязательно.',
        'password_mismatch': "Пароли не совпадают!",
    }

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
