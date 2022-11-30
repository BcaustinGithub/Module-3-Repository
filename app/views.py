from django.shortcuts import *
from django.http import HttpRequest
from django.http import HttpResponse
from app.forms import *
from .models import *
from django.contrib.auth import *


def base(request):
    ...

def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    return render(request, 'register.html', {'form':form})


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return render(request, 'base.html')
    return render(request, 'loginpage.html')

def lout(request):
    logout(request)
    return redirect('loginpage')

def checkout(request):
    return render(request, 'checkout.html')

def buyacar(request):
    return render(request, 'buyacar.html')

def sellcar(request):
    return render(request, 'sellacar.html')