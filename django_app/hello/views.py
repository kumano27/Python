# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    # メソッドチェーン
    data = Friend.objects.all().values()
    params = {
                'title': 'Hello',
                'data': data,
            }
    return render(request, 'hello/index.html' , params)