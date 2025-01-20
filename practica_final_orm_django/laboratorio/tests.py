from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio

class LaboratorioModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos iniciales para todas las pruebas
        cls.laboratorio = Laboratorio.objects.create(nombre="Laboratorio Prueba")

    def test_laboratorio_model_str(self):
        # Verificar que el método __str__ devuelva el nombre correctamente
        self.assertEqual(str(self.laboratorio), "Laboratorio Prueba")

    def test_laboratorio_data_matches(self):
        # Verificar que los datos en la base de datos coincidan con los configurados
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio Prueba")


class LaboratorioURLTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos iniciales
        cls.laboratorio = Laboratorio.objects.create(nombre="Laboratorio Prueba")

    def test_laboratorio_list_url(self):
        # Verificar que la URL de la lista devuelve un código HTTP 200
        response = self.client.get(reverse('laboratorio-list'))
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_create_url(self):
        # Verificar que la URL de creación devuelve un código HTTP 200
        response = self.client.get(reverse('laboratorio-create'))
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_update_url(self):
        # Verificar que la URL de actualización devuelve un código HTTP 200
        response = self.client.get(reverse('laboratorio-update', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_delete_url(self):
        # Verificar que la URL de eliminación devuelve un código HTTP 200
        response = self.client.get(reverse('laboratorio-delete', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)


class LaboratorioTemplateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos iniciales
        cls.laboratorio = Laboratorio.objects.create(nombre="Laboratorio Prueba")

    def test_laboratorio_list_template(self):
        # Verificar que la lista de laboratorios usa la plantilla correcta
        response = self.client.get(reverse('laboratorio-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio_list.html')
        self.assertContains(response, "Laboratorio Prueba")
        self.assertContains(response, "Agregar Laboratorio")

    def test_laboratorio_create_template(self):
        # Verificar que la página de creación usa la plantilla correcta
        response = self.client.get(reverse('laboratorio-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio_form.html')
        self.assertContains(response, "Nuevo Laboratorio")
        self.assertContains(response, "Guardar")

    def test_laboratorio_update_template(self):
        # Verificar que la página de actualización usa la plantilla correcta
        response = self.client.get(reverse('laboratorio-update', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio_form.html')
        self.assertContains(response, "Laboratorio Prueba")
        self.assertContains(response, "Guardar")

    def test_laboratorio_delete_template(self):
        # Verificar que la página de eliminación usa la plantilla correcta
        response = self.client.get(reverse('laboratorio-delete', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio_confirm_delete.html')
        self.assertContains(response, "¿Estás seguro que deseas eliminar")
        self.assertContains(response, "Laboratorio Prueba")
