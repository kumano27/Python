from django.db import models

# Create your models here.
class Squirtle(models.Model):
    CP = models.IntegerField()
    HP = models.IntegerField()
    SEX = models.BooleanField()
    WEIGHT = models.FloatField()
    HEIGHT = models.FloatField()
    MOVE1 = models.CharField(max_length=10)
    MOVE2 = models.CharField(max_length=10)
    
    def __str__(self):
        return '<Squirtle:CP=' + str(self.CP) + '>'