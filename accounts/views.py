from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages


import datetime
# Create your views here.
def regist_user(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponse('<h2> berhasil </h2>')
    else:
        forms = RegisterForm()
    return render(request, template_name, {'form':forms})

def login_user(request):
    template_name = 'accounts/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect ("/home/")
    else:
        form = LoginForm()
    return render(request, template_name, {'form': form})


class HomeUser( TemplateView):
    template_name = 'accounts/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeUser, self).get_context_data(**kwargs)
        context['display'] =  datetime.datetime.now()
        return context
