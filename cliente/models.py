from django.db import models
from django.contrib.auth.models import User
from endereco.models import Endereco
from contato.models import Contato

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    contato = models.OneToOneField(Contato, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)