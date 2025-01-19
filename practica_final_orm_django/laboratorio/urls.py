from django.urls import path
from laboratorio.views import LaboratorioListView
from laboratorio.views import DirectorGeneralListView
from laboratorio.views import ProductoListView

urlpatterns = [
    path('', LaboratorioListView.as_view(), name='laboratorio-list'),
    path('', DirectorGeneralListView.as_view(), name='director-general-list'),
    path('', ProductoListView.as_view(), name='producto-list'),
]
