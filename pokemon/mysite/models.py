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
    TrainerName = models.ForeignKey('Trainer',db_column = 'TrainerName', on_delete=models.CASCADE)
    
    def __str__(self):
        return '<Squirtle:CP=' + str(self.CP) + '>'
    
class Trainer(models.Model):
    TrainerName = models.CharField(max_length=20)
    TrainerLv = models.IntegerField()
    
    def __str__(self):
        return '<Trainer:TrainerName=' + str(self.TrainerName) + '>'