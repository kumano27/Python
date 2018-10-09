# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    # レコード数
    num = Friend.objects.all().count()
    # 最初のレコードを返す
    first = Friend.objects.all().first()
    # 最後のレコードを返す
    last = Friend.objects.all().last()
    data = [num, first, last]
    params = {
                'title': 'Hello',
                'data': data,
            }
    return render(request, 'hello/index.html' , params)