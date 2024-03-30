from django.db import models

# Create your models here.
class Endereco(models.Model):
    nome = models.CharField(max_length=255) 
    cep = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255)

    def __str__(self):
        endereco = self.logradouro + ', ' + str(self.numero)
        if self.complemento:
            endereco += ' - ' + self.complemento
        return endereco
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
