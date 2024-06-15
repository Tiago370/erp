from django.db import models
from produto.models import Produto

# Create your models here.
class Combo(Produto):

    produtos = models.ManyToManyField(Produto, related_name='combo_produtos')
    def __str__(self):
        return str(self.nome)