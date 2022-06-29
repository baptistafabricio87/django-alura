from django.contrib import admin

from .models import Receita

# Register your class filter
class ListReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'pessoa', 'publicar')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicar',)
    list_per_page = 2
    
# Register your models here.
admin.site.register(Receita, ListReceitas)
