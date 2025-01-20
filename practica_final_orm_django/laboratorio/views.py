from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio_list.html'
    context_object_name = 'laboratorios'

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    fields = ['nombre']
    template_name = 'laboratorio_form.html'
    success_url = reverse_lazy('laboratorio-list')

class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    fields = ['nombre']
    template_name = 'laboratorio_form.html'
    success_url = reverse_lazy('laboratorio-list')


class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio_confirm_delete.html'
    success_url = reverse_lazy('laboratorio-list')

class DirectorGeneralListView(ListView):
    model = DirectorGeneral
    template_name = "director_general_list.html"
    context_object_name = "directores_generales"


class ProductoListView(ListView):
    model = Producto
    template_name = "producto_list.html"
    context_object_name = "productos"
