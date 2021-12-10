from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from app.forms import ClienteForm, ServicoForm, TipoServicoForm, VeiculoForm
from app.models import Cliente, TipoServico, Veiculo, Servico

# Home


@login_required
def index(request):
    return render(request, 'home.html')

# Login


def login(request):
    return render(request, 'login.html')


# SERVIÇOS
def servico_list(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["dataset"] = Servico.objects.all()

    return render(request, "servico_list.html", context)


def servico_create(request):
    context = {}

    # create object of form
    form = ServicoForm(request.POST or None)

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
