from django.contrib import admin
from .models import Combo

# Register your models here.
class ComboAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'quantidade')
    search_fields = ('nome', 'descricao')

    filter_horizontal = ('produtos',)

admin.site.register(Combo, ComboAdmin)