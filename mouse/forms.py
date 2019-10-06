"""forms.py"""
from django.contrib.auth.models import User
from django import forms
from .models import Block

class AddBlock(forms.ModelForm):

    msg = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Hash'}))
    nonce = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Nonce'}))

    class Meta:
        """meta class"""
        model = Block
        fields = (
            'msg',
            'nonce'
        )