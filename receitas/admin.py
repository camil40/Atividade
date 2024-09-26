from django.contrib import admin
from receitas.models import Category, Recipe, Rating

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    list_display_links = ('id', 'categoria')
    search_fields = ('categoria',)
    list_per_page = 10

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'tempodepreparo', 'data_criacao', 'privacidade')
    list_filter = ['autor', 'privacidade', 'categoria']
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'ingredientes')
    list_per_page = 10

class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'receita', 'usuario', 'nota', 'comentario')
    list_display_links = ('id', 'receita')
    search_fields = ('receita__titulo', 'usuario__username', 'comentario')
    list_per_page = 10

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Rating, RatingAdmin)