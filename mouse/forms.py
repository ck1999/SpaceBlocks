"""forms.py"""
from django.contrib.auth.models import User
from django import forms
from .models import Block

class AddBlock(forms.ModelForm):

    msg = forms.CharField(label='',required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Hash', 'data-role':"input"}))
    nonce = forms.CharField(label='',required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nonce', 'data-role':"input", 'class': 'mt-3 mb-3'}))

    class Meta:
        model = Block
        fields = (
            'msg',
            'nonce'
        )