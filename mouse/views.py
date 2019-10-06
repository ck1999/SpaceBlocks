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

    if request.method == 'POST':
        form = AddBlock(request.POST)
        if form.is_valid():

            nonce_a = form.data['nonce']
            msg_a = form.data['msg']

            item = Block(hash = '0', nonce = nonce_a, date = datetime.datetime.now(), msg=msg_a)
            item.save()

    context = {}

    return render(request, 'add.html', context)

