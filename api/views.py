from rest_framework import viewsets
from api.models import Expense, Income
from api.serializer import ExpenseSerializer, IncomeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ExpensesViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Expenses"""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class IncomesViewSet(viewsets.ModelViewSet):
    """Exibindo todas as Incomes"""
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer