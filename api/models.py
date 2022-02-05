from django.db import models

class Default(models.Model):
    description = models.CharField(max_length=300, blank=False, null=False)
    value = models.FloatField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.description
    
class Expense(Default):
    pass

class Income(Default):
    pass
