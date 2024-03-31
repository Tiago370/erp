from django.db import models

# Create your models here.
class Endereco(models.Model):
    nome_endereco = models.CharField(max_length=255, blank=True) 
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=255, blank=True)

    def __str__(self):
        endereco = self.logradouro + ', ' + str(self.numero)
        if self.complemento:
            endereco += ' - ' + self.complemento
        return endereco
    
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
