from django.db import models


class Veiculo(models.Model):
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50, verbose_name='Modelo')
    ano = models.IntegerField(verbose_name='Ano')
    placa = models.CharField(max_length=8, unique=True, verbose_name='Placa')
    cor = models.CharField(max_length=30, verbose_name='Cor')
    proprietario = models.CharField(max_length=100, verbose_name='Proprietário')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['marca', 'modelo']
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'


class Manutencao(models.Model):
    TIPO_CHOICES = [
        ('manutencao', 'Manutenção Geral'),
        ('troca_pneus', 'Troca de Pneus'),
        ('troca_oleo', 'Troca de Óleo'),
        ('revisao', 'Revisão'),
        ('freios', 'Freios'),
        ('outro', 'Outro'),
    ]

    veiculo = models.ForeignKey(
        Veiculo,
        on_delete=models.CASCADE,
        related_name='manutencoes',
        verbose_name='Veículo'
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name='Tipo de Serviço')
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    data = models.DateField(verbose_name='Data do Serviço')
    quilometragem = models.IntegerField(verbose_name='Quilometragem', null=True, blank=True)
    custo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Custo', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    class Meta:
        ordering = ['-data']
        verbose_name = 'Manutenção'
        verbose_name_plural = 'Manutenções'

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.veiculo.placa} ({self.data})'