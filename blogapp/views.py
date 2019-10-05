from django.shortcuts import render
import englishrandomwords
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
# Create your views here.
