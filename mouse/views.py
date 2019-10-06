from django.shortcuts import render
import mousesite
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
# Create your views here.

def blocks(request):
    """list of blocks"""
    return render(request, 'blocks.html', context)