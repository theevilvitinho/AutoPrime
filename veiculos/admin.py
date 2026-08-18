from django.contrib import admin
from .models import Veiculo, Manutencao

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'placa', 'cor', 'proprietario', 'is_active')
    search_fields = ('marca', 'modelo', 'placa', 'proprietario')
    list_filter = ('marca', 'is_active', 'ano')


@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'tipo', 'data', 'quilometragem', 'custo')
    search_fields = ('veiculo__placa', 'veiculo__proprietario')
    list_filter = ('tipo', 'data')