from django.contrib import admin
from .models import MeioPagamento

# Register your models here.
class MeioPagamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_trasacionado')
    search_fields = ('nome',)


admin.site.register(MeioPagamento, MeioPagamentoAdmin)