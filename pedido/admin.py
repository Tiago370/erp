from django.contrib import admin
from .models import Pedido

# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('cliente_nome',)

    filter_horizontal = ('produtos', 'combos')


admin.site.register(Pedido, PedidoAdmin)