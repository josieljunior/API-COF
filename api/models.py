from django.db import models

class Default(models.Model):
    descricao = models.CharField(max_length=300, blank=False, null=False)
    valor = models.FloatField(blank=False, null=False)
    data = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.descricao
    
class Despesa(Default):
    pass

class Receita(Default):
    pass
