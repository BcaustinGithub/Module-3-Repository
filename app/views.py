from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from app.forms import *
from .models import *
from django.contrib.auth import *

def base(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(username=username, password=password)
        user.save()
        return render(request, 'base.html')
    else:
        return render(request, '')