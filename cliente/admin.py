from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('user', 'endereco', 'contato')
    search_fields = ('user__username', 'endereco__logradouro', 'contato__whatsapp')


admin.site.register(Cliente, ClienteAdmin)