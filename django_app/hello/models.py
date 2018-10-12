from django.db import models
from django.core.validators import RegexValidator
# モデルに関する処理を記述するもの
# Create your models here.

class Friend(models.Model):
    # a～zの小文字だけを入力許可
    name = models.CharField(max_length=100,validators=[RegexValidator(r'^[a-z]*$')])
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField()
    birthday = models.DateField()
    
    # __str__ テキストの値を返す為のもの
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'