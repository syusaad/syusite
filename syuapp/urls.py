from django.urls import path
from syuapp.views import *

urlpatterns = [
    path('', index, name ='index'),
]