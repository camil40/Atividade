from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100)

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    mododepreparo = models.TextField(blank=True, null=True)
    tempodepreparo = models.TimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    privacity = models.BooleanField(default=True)
    

    
    
class Rating(models.Model):
    receita = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(null=True)
    coment = models.TextField(blank=True, null=True)