from django.db import models

# Create your models here.

class Coupons(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    offer = models.IntegerField(default=10)
    
    
    code = models.TextField(unique=True)
   
    conditions = models.TextField(default=000000)
    
    
    content = models.TextField()
    slug = models.CharField(max_length=130,unique=True)
    
    
    
    def __str__(self):
        return self.name +' by '
    
    
