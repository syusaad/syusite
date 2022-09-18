from django.urls import path
from django.shortcuts import redirect
from syuapp.views import *

urlpatterns = [
    path('', lambda req: redirect(index)), # redirect root to index
    path('home/', index, name='index'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
]