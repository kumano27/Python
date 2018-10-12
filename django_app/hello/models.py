# re -> Python正規化モジュール
import re
from django.db import models
from django.core.validators import ValidationError
# モデルに関する処理を記述するもの
# Create your models here.

def number_only(value):
    # 正規表現モジュールと引数に指定したテキストのパターンがマッチングするか？
    if(re.match(r'^[0-9]*$', value) == None):
        # マッチングしたら...
        raise ValidationError(
                    '%(value)s is not Number!', params={'value': value},
                )

class Friend(models.Model):
    name = models.CharField(max_length=100,validators=[number_only])
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField()
    birthday = models.DateField()
    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'
    
class Message(models.Model):
    # ForeignKey の項目。on_delete -> 削除する際の設定
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    # タイトルのテキストを保管するためのもの
    title = models.CharField(max_length=100)
    # コンテンツを保管するためのもの(メッセージ本体)
    contemt = models.CharField(max_length=300)
    # 投稿した日時を保管
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '<Message:id=' + str(self.id) + ', ' + self.title + '(' + str(self.pub_date) + ')>'
    
    class Meta:
        ordering = ('pub_date',)
