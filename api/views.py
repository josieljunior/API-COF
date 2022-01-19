from rest_framework import viewsets
from api.models import Despesa, Receita
from api.serializer import DespesaSerializer, ReceitaSerializer

class DespesasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer