from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  
    search_fields = ('nombre',) 


@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio')
    search_fields = ('nombre', 'laboratorio__nombre')
    autocomplete_fields = ('laboratorio',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('laboratorio', 'f_fabricacion')
    search_fields = ('nombre', 'laboratorio__nombre')
    autocomplete_fields = ('laboratorio',)

admin.site.site_header = "Administración de Laboratorios"
admin.site.site_title = "Panel Administrativo"
admin.site.index_title = "Gestión de Laboratorio"
