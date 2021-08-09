import datetime

from django.contrib.auth import login, authenticate
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from mouse.forms import AddBlock, SignUpForm
from mouse.models import Block as BlockModel


class IndexView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.template_name = 'index.html'

    def get(self, request: HttpRequest) -> render:
        return render(request, self.template_name)


class BlockView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.template_name_list = 'blocks.html'
        self.template_name_add_block = 'add.html'
        self.context = {}

    def get(self, request: HttpRequest) -> render:
        blocks = BlockModel.objects.all()
        self.context = {'blocks': blocks}

        return render(request, self.template_name_list, self.context)

    def post(self, request: HttpRequest) -> render:
        form = AddBlock(request.POST)
        if form.is_valid():
            nonce_a = form.data['nonce']
            msg_a = form.data['msg']
            latest_id = BlockModel.objects.latest('id').id
            item = BlockModel(nonce=int(nonce_a), time=datetime.datetime.now(), msg=msg_a)
            item.hash = item.calc_hash(BlockModel.objects.get(id=latest_id).hash)
            if item.validate():
                item.save()
        return render(request, self.template_name_add_block, {'form': form})


class SignupView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.template_name = 'registration/signup.html'

    def get(self, request: HttpRequest) -> render:
        return render(request, self.template_name, {'form': SignUpForm()})

    def post(self, request: HttpRequest):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            return self.get(request)


class ProfileView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.template_name = 'registration/profile.html'

    def get(self, request: HttpRequest) -> render:
        context = {'user': request.user}
        return render(request, self.template_name, context)
