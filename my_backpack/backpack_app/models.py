from django.db import models

# Create your models here.

class MyBackpack(models.Model):
    id = models.AutoField (primary_key=True) 
    card_name = models.CharField(max_length=250)
    is_adding = models.BooleanField(null=False)
    
    def __str__(self):
        return f"Card Name: {self.card_name}"
    

