from django.contrib import admin
from .models import Contato

# Register your models here.
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('whatsapp', 'email', 'nome_contato')

admin.site.register(Contato, ContatoAdmin)