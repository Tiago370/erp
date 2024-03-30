from django.contrib import admin

# Register your models here.
from .models import Endereco

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logradouro', 'numero', 'complemento', 'cep')

admin.site.register(Endereco, EnderecoAdmin)