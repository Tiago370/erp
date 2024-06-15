from django.db import models

# Create your models here.
class Entregador(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, default="")
    placa = models.CharField(max_length=8, default="")
    disponibilidade = models.CharField(max_length=10, choices={
        ('desativado', 'Desativado'),
        ('ocupado', 'Ocupado'),
        ('disponivel', 'Disponível')}, default="disponível")
    
    def __str__(self):
        return str(self.nome)