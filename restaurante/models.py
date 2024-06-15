from django.db import models
from django.contrib.auth.models import User
from endereco.models import Endereco
from contato.models import Contato

# Create your models here.
class Restaurante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE)
    cnpj = models.CharField(max_length=14)
    especializacao = models.CharField(max_length=10, choices={
        ('massas', 'Massas'),
        ('carnes', 'Carnes'),
        ('pizza', 'Pizza')})
    def __str__(self):
        return str(self.user)