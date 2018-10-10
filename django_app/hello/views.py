# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm

def index(request):
    data = Friend.objects.all()
    params = {
                'title': 'Hello',
                'data': data,
            }
    return render(request, 'hello/index.html' , params)

# create model
def create(request):
    # POST送信されたか確認
    if (request.method == 'POST'):
        # Friend クラスのインスタンス作成(初期状態のインスタンス)
        obj = Friend()
        # FriendForm インスタンス作成
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
                'title': 'Helo',
                'form': FriendForm(),
            }
    return render(request, 'hello/create.html',params)