from re import search
from django.contrib import admin
from api.models import Despesa, Receita

class Despesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data', 'valor')
    list_display_link = ('id', 'decricao')
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(Despesa, Despesas)

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data', 'valor')
    list_display_link = ('id', 'decricao')
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(Receita, Receitas)