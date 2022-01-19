from rest_framework import viewsets
from api.models import Despesa, Receita
from api.serializer import DespesaSerializer, ReceitaSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class DespesasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as despesas"""
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ReceitasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as receitas"""
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer