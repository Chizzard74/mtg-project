from django.db import models

# Create your models here.

class MyBackpack(models.Model):
    card_name = models.CharField(max_length=250)
    image_string = models.CharField(max_length=250)
    price = models.FloatField()
    
    def __str__(self):
        return f"Card Name: {self.card_name}\nCard Price: {self.price}"
    

