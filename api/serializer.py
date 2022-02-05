from rest_framework import serializers
from api.models import Expense, Income
from rest_framework.validators import UniqueForMonthValidator

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        validators = [
            UniqueForMonthValidator(
                queryset = Expense.objects.all(),
                field = 'description',
                date_field = 'date'
            )
        ]
        
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
        validators = [
            UniqueForMonthValidator(
                queryset = Income.objects.all(),
                field = 'description',
                date_field = 'date'
            )
        ]