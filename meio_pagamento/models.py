from django.db import models

# Create your models here.
class MeioPagamento(models.Model):
    nome = models.CharField(max_length=100)
    valor_trasacionado = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return str(self.nome)