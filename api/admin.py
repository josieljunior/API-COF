from re import search
from django.contrib import admin
from api.models import Despesa, Receita

class Default(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data', 'valor')
    list_display_link = ('id', 'decricao')
    search_fields = ('id',)
    list_per_page = 20

class Despesas(admin.ModelAdmin):
    pass


class Receitas(admin.ModelAdmin):
    pass

admin.site.register(Despesa, Despesas)
admin.site.register(Receita, Receitas)