# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirtle

def index(request):
    data = Squirtle.objects.all()
    params = {
                'data': data,
            }
    return render(request, 'mysite/index.html',params)