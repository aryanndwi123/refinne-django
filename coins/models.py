from django.db import models

# Create your models here.

class Coins(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    coins = models.IntegerField(default=10)
    
    
    
    def __str__(self):
        return self.username +' by '
    
    
