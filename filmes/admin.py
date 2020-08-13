from django.contrib import admin
from .models import Lancamentos, Misturados

@admin.register(Lancamentos)
class LancamentosModel(admin.ModelAdmin):
    list_display = ("nome_film", "genero", "data_cria", "data_act", "Activ")
    
@admin.register(Misturados)
class MisturadosModel(admin.ModelAdmin):
    list_display = ("nome_film", "genero", "data_cria", "data_act", "Activ")
