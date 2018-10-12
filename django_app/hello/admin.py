from django.contrib import admin
# 管理者ツールの為の物
# Register your models here.
from .models import Friend, Message

admin.site.register(Friend)
admin.site.register(Message)