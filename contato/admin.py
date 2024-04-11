from django.contrib import admin
from .models import Contato
from .forms import ContatoFormAdmin

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'email', 'nome_contato')

    form = ContatoFormAdmin

    class Media:
        js = ('jquery.mask.min.js','custom.js',)

admin.site.register(Contato, ContatoAdmin)