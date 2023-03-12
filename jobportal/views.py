from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import *

# candidates view


def home(request):
    context = {
        'home_page': "active",
    }
    return render(request, 'index.html', context)
