"""forms.py"""
from django.contrib.auth.models import User
from django import forms
from .models import Block

class AddBlock(forms.ModelForm):

    msg = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Hash', 'data-role':"input"}))
    nonce = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Nonce', 'data-role':"input"}))

    class Meta:
        model = Block
        fields = (
            'msg',
            'nonce'
        )