from django.shortcuts import render
from django.http import HttpResponse
from . import urls

def index(request):
    return render(request, 'Blog/index.html')

# Create your views here.
