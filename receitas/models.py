from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    categoria = models.CharField(max_length=100)

class Recipe(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    ingredientes = models.TextField(blank=True, null=False)
    mododepreparo = models.TextField(blank=True, null=False, default=True)
    tempodepreparo = models.TimeField(blank=True, null=False)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    privacidade = models.BooleanField(default=True)

class Rating(models.Model):
    receita = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(null=True)
    comentario = models.TextField(blank=True, null=True)