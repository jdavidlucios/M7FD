from django.urls import path
from laboratorio.views import LaboratorioListView
from laboratorio.views import DirectorGeneralListView
from laboratorio.views import ProductoListView
from .views import (
    LaboratorioListView,
    LaboratorioCreateView,
    LaboratorioUpdateView,
    LaboratorioDeleteView
)

urlpatterns = [
    path('laboratorios', LaboratorioListView.as_view(), name='laboratorio-list'),
    path('crear', LaboratorioCreateView.as_view(), name='laboratorio-create'),
    path('editar', LaboratorioUpdateView.as_view(), name='laboratorio-update'),
    path('eliminar', LaboratorioDeleteView.as_view(), name='laboratorio-delete'),
    path('director-general', DirectorGeneralListView.as_view(), name='director-general-list'),
    path('productos', ProductoListView.as_view(), name='producto-list'),
    
]
