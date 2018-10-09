# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm

def index(request):
    params = {
                'title': 'Hello',
                'message': 'all friends.' ,
                'form': HelloForm(),
                'data': [],
            }
    # POSTされたかを判定
    if(request.method == 'POST'):
        # フォームから送られた値を元に指定のIDレコードをモデルインスタンスとして取り出す
        num=request.POST['id']
        item = Friend.objects.get(id=num)   # IDの値がnumのレコードを1つだけ取り出す
        params['data']=[item]
        params['form']=HelloForm(request.POST)
    else:
        params['data']=Friend.objects.all()
    return render(request, 'hello/index.html' , params)