from datetime import datetime, timedelta
from decimal import Decimal
from urllib.parse import parse_qs, urlparse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from app.forms import ClienteForm, ServicoForm, TipoServicoForm, VeiculoForm, AcertoForm
from app.models import Cliente, TipoServico, Veiculo, Servico, ServicoStatus, Acerto

# Home


@login_required
def index(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    date_from = datetime.now() - timedelta(days=3)
    context["servicos"] = Servico.objects.filter(data_entrada__gte=date_from).all()
    return render(request, 'home.html',context)

# Login


def login(request):
    return render(request, 'login.html')


# SERVIÇOS
def financeiro_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    status = request.GET.get("status")
    data_inicial_request = request.GET.get("dataInicial")
    data_final_request = request.GET.get("dataFinal")

    # add the dictionary during initialization
    queryset = Servico.objects.all()


    if (data_inicial_request is not None and data_inicial_request != '') and (data_final_request is not None and data_final_request != ''):
        data_inicial = datetime.strptime(data_inicial_request, '%Y-%m-%d')
        data_final = datetime.strptime(data_final_request, '%Y-%m-%d')

        queryset = queryset.filter(data_entrada__gte=data_inicial).filter(data_entrada__lte=data_final)

    final_list = list(queryset)

    if status != None and status != '':
        if(status == 'pago'):
            ids = [service.pk for service in final_list if service.get_valor_restante() == 0]
            final_list = list(queryset.filter(id__in=ids))
        else:
            ids = [service.pk for service in final_list if service.get_valor_restante() > 0]
            final_list = list(queryset.filter(id__in=ids))

    context["dataset"] = final_list
    context["status_list"] = ServicoStatus.choices()    

    context["status"] = status    
    context["data_inicial"] = data_inicial_request    
    context["data_final"] = data_final_request    

    return render(request, "financeiro_list.html", context)

# SERVIÇOS
def servico_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    status = request.GET.get("status")
    andamento = request.GET.get("andamento")
    data_inicial_request = request.GET.get("dataInicial")
    data_final_request = request.GET.get("dataFinal")

    # add the dictionary during initialization
    queryset = Servico.objects.all()
    
    if andamento == 'true':
        andamento = True if 'true' else False
        if andamento:
            queryset = queryset.filter(status__lt=5)
        else:
            queryset = queryset.filter(status__gt=4)
            
    if status != None and status != '':
        queryset = queryset.filter(status=status)
    if (data_inicial_request is not None and data_inicial_request != '') and (data_final_request is not None and data_final_request != ''):
        data_inicial = datetime.strptime(data_inicial_request, '%Y-%m-%d')
        data_final = datetime.strptime(data_final_request, '%Y-%m-%d')

        queryset = queryset.filter(data_entrada__gt=data_inicial).filter(data_entrada__lt=data_final)

    context["dataset"] = list(queryset)
    context["status_list"] = ServicoStatus.choices()    

    context["status"] = status    
    context["data_inicial"] = data_inicial_request    
    context["data_final"] = data_final_request    

    return render(request, "servico_list.html", context)


def servico_create(request):
    context = {}

    # create object of form
    form = ServicoForm(request.POST or None)

    tipos = request.POST.getlist("itens")

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect("/servicos")

    context['form'] = form
    return render(request, "servico_create.html", context)


def servico_edit(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Servico, id=id)

    # pass the object as instance in form
    form = ServicoForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/servicos")

    # add form dictionary to context
    context["form"] = form

    return render(request, "servico_edit.html", context)


def servico_delete(_, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Servico, id=id)

    obj.delete()
    return HttpResponseRedirect("/servicos")

def acerto_create(request, servico_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    servico_existente = get_object_or_404(Servico, id=servico_id)
    acertos_ja_feitos = Acerto.objects.filter(servico_id = servico_id)
    context["valor_total"] = servico_existente.get_total_itens_com_desconto()
    context["valor_ja_acertado"] = servico_existente.get_total_acertado()

    obj = Acerto()

    obj.servico = servico_existente
    obj.valor = servico_existente.get_valor_restante()
    obj.valor_comissao = round(obj.valor * Decimal(0.1), 2)

    # pass the object as instance in form
    form = AcertoForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # add form dictionary to context
    context["form"] = form
    

    return render(request, "acerto_create.html", context)

# CLIENTES
def cliente_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Cliente.objects.all()

    return render(request, "cliente_list.html", context)


def cliente_create(request):
    context = {}

    # create object of form
    form = ClienteForm(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect("/clientes")

    context['form'] = form
    return render(request, "cliente_create.html", context)


def cliente_edit(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Cliente, id=id)

    # pass the object as instance in form
    form = ClienteForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/clientes")

    # add form dictionary to context
    context["form"] = form

    return render(request, "cliente_edit.html", context)


def cliente_delete(_, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Cliente, id=id)

    obj.delete()
    return HttpResponseRedirect("/clientes")

# VEÍCULOS
def veiculo_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Veiculo.objects.all()

    return render(request, "veiculo_list.html", context)


def veiculo_create(request):
    context = {}

    # create object of form
    form = VeiculoForm(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect("/veiculos")

    context['form'] = form
    return render(request, "veiculo_create.html", context)


def veiculo_edit(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Veiculo, id=id)

    # pass the object as instance in form
    form = VeiculoForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/veiculos")

    # add form dictionary to context
    context["form"] = form

    return render(request, "veiculo_edit.html", context)


def veiculo_delete(_, id):
    # fetch the object related to passed id
    obj = get_object_or_404(Veiculo, id=id)

    obj.delete()
    return HttpResponseRedirect("/veiculos")

# Tipo de serviço

def tipo_servico_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = TipoServico.objects.all()

    return render(request, "tipo_servico_list.html", context)


def tipo_servico_create(request):
    context = {}

    # create object of form
    form = TipoServicoForm(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return HttpResponseRedirect("/tipos-servico")

    context['form'] = form
    return render(request, "tipo_servico_create.html", context)


def tipo_servico_edit(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(TipoServico, id=id)

    # pass the object as instance in form
    form = TipoServicoForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/tipos-servico")

    # add form dictionary to context
    context["form"] = form

    return render(request, "tipo_servico_edit.html", context)


def tipo_servico_delete(_, id):
    # fetch the object related to passed id
    obj = get_object_or_404(TipoServico, id=id)

    obj.delete()
    return HttpResponseRedirect("/tipos-servico")

# Serviço


@login_required
def novo_servico(request):
    return render(request, 'novo_servico.html')


@login_required
def servicos_efetuar(request):
    return render(request, 'servicos_efetuar.html')
