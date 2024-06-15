from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente
from produto.models import Produto
from combo.models import Combo
from endereco.models import Endereco
from entregador.models import Entregador
from meio_pagamento.models import MeioPagamento

# Create your models here.
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    combos = models.ManyToManyField(Combo, related_name='pedidos', blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, default="")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE, default="")
    meio_pagamento = models.ForeignKey(MeioPagamento, on_delete=models.CASCADE, null=True)
    
    def cliente_nome(self):
        # Logic to calculate or retrieve the customer name
        return self.cliente.user.first_name + ' ' + self.cliente.user.last_name
    def __str__(self):
        return str(self.cliente_nome())