from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from app.forms import TipoServicoForm
from app.models import TipoServico

# Home


@login_required
def index(request):
    return render(request, 'home.html')

# Login


def login(request):
    return render(request, 'login.html')

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
