import datetime

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from mouse.forms import AddBlock, SignUpForm
from mouse.models import Block as BlockModel


def index(request):
    return render(request, 'index.html')


# Create your views here.

def blocks(request):
    blocks = BlockModel.objects.all()
    context = {'blocks': blocks}
    return render(request, 'blocks.html', context)


@login_required
def add_block(request):
    f = AddBlock(request.POST)
    if request.method == 'POST':
        if f.is_valid():
            nonce_a = f.data['nonce']
            msg_a = f.data['msg']
            latest_id = BlockModel.objects.latest('id').id
            item = BlockModel(nonce=int(nonce_a), time=datetime.datetime.now(), msg=msg_a)
            item.hash = item.calc_hash(BlockModel.objects.get(id=latest_id).hash)
            if item.validate():
                item.save()
    return render(request, 'add.html', {'form': f})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def account(request):
    context = {
        'user': request.user,
    }
    return render(request, 'registration/profile.html', context)
