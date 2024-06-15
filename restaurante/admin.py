from django.contrib import admin
from .models import Restaurante

# Register your models here.
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('user', 'endereco', 'contato', 'especializacao',)
    search_fields = ('user__username', 'endereco__logradouro', 'contato__whatsapp')


admin.site.register(Restaurante, RestauranteAdmin)