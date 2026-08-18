from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Veiculo
from .forms import VeiculoForm


def home(request):
    return render(request, 'home.html')

@login_required
def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'veiculo_list.html', {'veiculos': veiculos})


@login_required
def veiculo_create(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculo_list')
    else:
        form = VeiculoForm()
    return render(request, 'veiculo_form.html', {'form': form, 'titulo': 'Cadastrar Veículo'})


@login_required
def veiculo_update(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            return redirect('veiculo_list')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculo_form.html', {'form': form, 'titulo': 'Editar Veículo'})


@login_required
def veiculo_delete(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculo_list')
    return render(request, 'veiculo_confirm_delete.html', {'veiculo': veiculo})



def veiculo_consulta(request):
    veiculo = None
    manutencoes = None
    erro = None

    if request.method == 'POST':
        modelo = request.POST.get('modelo', '').strip()
        placa = request.POST.get('placa', '').strip().upper()

        try:
            veiculo = Veiculo.objects.get(
                modelo__iexact=modelo,
                placa__iexact=placa
            )
            manutencoes = veiculo.manutencoes.all()
        except Veiculo.DoesNotExist:
            erro = 'Nenhum veículo encontrado com esse modelo e placa. Verifique os dados.'

    return render(request, 'veiculo_consulta.html', {
        'veiculo': veiculo,
        'manutencoes': manutencoes,
        'erro': erro,
    })