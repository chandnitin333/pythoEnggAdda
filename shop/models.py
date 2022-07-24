from faulthandler import is_enabled
from math import fabs
from tkinter.tix import Tree
from turtle import update
from click import option
from django.db import models

# Create your models here.

class BookTable(models.Model):
    name    = models.CharField("Full Name",max_length=200,blank=True,null=True)
    email   = models.EmailField()
    phone   = models.CharField(max_length=20, blank = True, null = True)
    message = models.TextField(blank=True, null=True)
    people  = models.IntegerField()
    bdate   = models.DateField("Booking Date", auto_now_add=False)
    btime   = models.TimeField("b[king Time", auto_now_add=False)
    
    def __str__(self) -> str:
        return self.name
    
class Food(models.Model):
    food_name = models.CharField("Food Name", max_length=200,blank=False,null=False)
    food_description = models.TextField(blank=True,null=True)
    food_price = models.DecimalField(max_digits=5,decimal_places=2 ,null=False)
    food_category =models.CharField("category",max_length=100, blank=False,null=False)
    is_enabled = models.BooleanField()
    is_deleted = models.BooleanField()
    created_at = models.DateTimeField(auto_created=True)
    update_at  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.food_name
    
    
    