from re import search
from django.contrib import admin
from api.models import Expense, Income

class Default(admin.ModelAdmin):
    list_display = ('id', 'description', 'date', 'value')
    list_display_link = ('id', 'description')
    search_fields = ('id',)
    list_per_page = 20

class Expenses(admin.ModelAdmin):
    pass


class Incomes(admin.ModelAdmin):
    pass

admin.site.register(Expense, Expenses)
admin.site.register(Income, Incomes)