from django.db import models
import random

def generate_default_otp():
    return str(random.randint(100000, 999999))

# Create your models here.


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=128, choices= (
        ('Electronics', 'Electronics'),
        ('Clothing', 'Clothing'),
        ('Electrical', 'Electrical'),
        ('Sports', 'Sports'),
        ('Grooming', 'Grooming')
    ))
    active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, null = True)
    otp = models.CharField(max_length=6, null = True) 
    
    def __str__(self):
        return self.type

class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    prod_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name