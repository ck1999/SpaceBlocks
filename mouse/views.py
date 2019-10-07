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
    blocks = Block.objects.all()
    context = {'blocks': blocks}
    return render(request, 'blocks.html', context)

def add_block(request):
    f = AddBlock(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            nonce_a = f.data['nonce']
            msg_a = f.data['msg']
            item = Block(nonce = int(nonce_a), time = datetime.datetime.now(), msg=msg_a)
            item.hash = item.calc_hash(Block.objects.get(id = (Block.objects.latest('id') - 1)))
            item.save() 
    
    return render(request, 'add.html', {'form': f})
