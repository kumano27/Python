from django.db import models
# モデルに関する処理を記述するもの
# Create your models here.

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
    # __str__ テキストの値を返す為のもの
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'