# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import HelloForm

def index(request):
    data = Friend.objects.all()
    params = {
                'title': 'Hello',
                'data': data,
            }
    return render(request, 'hello/index.html' , params)

# create model
def create(request):
    params = {
                'title': 'Hello',
                'form': HelloForm(),
            }
    # POST送信されたか確認
    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        gender = 'gender' in request.POST
        age = int(request.POST['age'])
        birth = request.POST['birthday']
        
        # 上記の値を元に、Friendインスタンス作成
        friend = Friend(name=name,mail=mail,gender=gender,age=age,birthday=birth)
        # インスタンスを保存
        friend.save()
        # /hello にリダイレクト
        return redirect(to='/hello')
    return render(request, 'hello/create.html',params)