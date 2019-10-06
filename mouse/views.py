from django.shortcuts import render
import mousesite
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
# Create your views here.

def blocks(request):
    """list of blocks"""
    return render(request, 'blocks.html')

def add_block(request):

    context = {'menu:': get_menu_context(request)}

    if request.method == 'POST':
        form = AddBlock(request.POST)
        if form.is_valid():

            nonce_a = form.data['nonce']
            msg_a = form.data['msg']

            item = Block(hash = '0', nonce = nonce_a, date = datetime.datetime.now(), msg=msg_a)
            item.save()
    
    return render(request, 'add.html', context)

