"""forms.py"""
from django.contrib.auth.models import User
from django import forms
from .models import Block

class AddBlock(forms.ModelForm):

    msg = forms.CharField(label='',required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Msg', 'data-role':"input"}))
    nonce = forms.CharField(label='',required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nonce', 'data-role':"input", 'class': 'mt-2 mb-2'}))

    class Meta:
        model = Block
        fields = (
            'msg',
            'nonce'
        )