from django.db import models

# Create your models here.
class Contato(models.Model):
    nome_contato = models.CharField(max_length=255, blank=True) 
    whatsapp = models.CharField(max_length=15)
    email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        contato = self.whatsapp
        if self.nome_contato:
            contato += ' (' + self.nome + ')'
        return contato