from django.contrib import admin

from .forms import EnderecoFormAdmin

# Register your models here.
from .models import Endereco

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logradouro', 'numero', 'complemento', 'cep')
    form = EnderecoFormAdmin
    class Media:
        js = ('jquery.mask.min.js',
              'custom.js',
              )

admin.site.register(Endereco, EnderecoAdmin)