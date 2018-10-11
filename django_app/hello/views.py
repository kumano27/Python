# 画面表示に関するもの
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from .forms import FindForm

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

def edit(request, num):
    # インスタンスの取得 -> 引数id
    obj = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        # instance 引数に get で取得したインスタンスを指定
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
                'title': 'Hello',
                'id':num,
                'form': FriendForm(instance=obj),
            }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if(request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
                'title': 'Hello',
                'id': num,
                'obj': friend,
            }
    return render(request, 'hello/delete.html', params)

def find(request):
    if(request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Friend.objects.filter(name=str)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
                'title':'Hello',
                'message':msg,
                'form':form,
                'data':data,
            }
    return render(request, 'hello/find.html', params)
        