from django.urls import path
from app.views import *
from django.contrib.admin import site

urlpatterns = [
    path('sellacar', sellcar),
    path('buyacar', buyacar),
    path('checkout', checkout),
    path('registerpage', registerpage),
    path('loginpage', base),
    path('', loginpage, name='loginpage'),
    path('logout', lout, name='lout'),
    path('admin/', site.urls),
]