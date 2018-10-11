from django.db import models
from django.core.validators import MinLengthValidator
# モデルに関する処理を記述するもの
# Create your models here.

class Friend(models.Model):
    # 最小文字数10文字以内だとエラー
    name = models.CharField(max_length=100,validators=[MinLengthValidator(10)])
    # 最小文字数10文字以内だとエラー
    mail = models.EmailField(max_length=200,validators=[MinLengthValidator(10)])
    gender = models.BooleanField()
    age = models.IntegerField()
    birthday = models.DateField()
    
    # __str__ テキストの値を返す為のもの
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'