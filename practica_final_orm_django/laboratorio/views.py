from django.views.generic import ListView
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio_list.html'
    context_object_name = 'laboratorios'

class DirectorGeneralListView(ListView):
    model = DirectorGeneral
    template_name = "director_general_list.html"
    context_object_name = "directores_generales"


class ProductoListView(ListView):
    model = Producto
    template_name = "producto_list.html"
    context_object_name = "productos"
