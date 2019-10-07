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

            item = Block(hash = '0', nonce = int(nonce_a), time = datetime.datetime.now(), msg=msg_a)
            item.save(commit=False) 
    
    return render(request, 'add.html', {'form': f})

def block_list(request):
    blocks = Block.objects()
    blocks.append(Block('000000000000000', 0,  'MasterBlock', datetime.datetime.now(),))
    return render(request, 'blocks.html', {'blocks': blocks})