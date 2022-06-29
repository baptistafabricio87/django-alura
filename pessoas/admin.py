from django.contrib import admin
from .models import Pessoa

# Create your class list
class ListPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page: 2

# Register your models here.
admin.site.register(Pessoa, ListPessoas)