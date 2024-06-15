from django.contrib import admin
from .models import Produto

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'quantidade')
    search_fields = ('user__username', 'endereco__logradouro', 'contato__whatsapp')


admin.site.register(Produto, ProdutoAdmin)