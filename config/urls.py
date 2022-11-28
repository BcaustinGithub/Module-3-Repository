from django.urls import path
from app.views import *
from django.contrib.admin import site

urlpatterns = [
    path('', base),
    path('admin/', site.urls),
]
