from django.shortcuts import render
import mousesite
from django.http import HttpResponse
from mouse.forms import AddBlock
from mouse.models import Block
import datetime

def index(request):
    return render(request, 'index.html')
# Create your views here.

def blocks(request):

    return render(request, 'blocks.html')

def add_block(request):
    f = AddBlock(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            nonce_a = f.data['nonce']
            msg_a = f.data['msg']

            item = Block(hash = '0', nonce = nonce_a, date = datetime.datetime.now(), msg=msg_a)
            item.save() 
    
    return render(request, 'add.html', {'form': f})

def block_list(request):
    blocks = Block.objects()
    return render(request, 'blocks.html', {'blocks': block_list})

from django.contrib.auth.models import User

def createsuper():
    u = User(username='AdminPanel')
    u.set_password('nhjkghbdtn!1')
    u.is_superuser = True
    u.is_staff = True
    u.save()