from django.contrib import admin
from .models import Entregador

# Register your models here.
class EntregadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'disponibilidade')
    search_fields = ('nome',)

admin.site.register(Entregador, EntregadorAdmin)