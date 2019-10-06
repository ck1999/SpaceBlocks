from django.shortcuts import render
import mousesite
from django.http import HttpResponse
from .models import *
from forms import *

def index(request):
    return render(request, 'index.html')
# Create your views here.

def blocks(request):
    """list of blocks"""
    return render(request, 'blocks.html')

def add_block(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            AddBlock = form.save(commit=False)
            AddBlock.msg = '123'
    return render(request, 'blocks.html')