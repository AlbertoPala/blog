from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Publicaciones

# Create your tests here.
class PruebasBlog(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username = 'usuarioprueba',
            email = 'prueba@gmail.com',
            password = 'secreto'
        )

        self.pub = Publicaciones.objects.create(
            titulo = 'Un buen titulo',
            cuerpo = 'Muy buen contenido',
            autor = self.usuario
        )
    
    def test_representacion_cadenas(self):
        pub = Publicaciones(titulo='Un titulo simple') #objeto de la clase publicaciones
        self.assertEqual(str(pub), pub.titulo) #comparando los titulos

    def test_contenido_publicacion(self):
        self.assertEqual(f'{self.pub.titulo}', 'Un buen titulo') #cadena con formato 'f'
        self.assertEqual(f'{self.pub.autor}', 'usuarioprueba')
        self.assertEqual(f'{self.pub.cuerpo}', 'Muy buen contenido')

    def test_vista_lista_publicaciones(self):
        respuesta = self.client.get(reverse('inicio')) #verificamos que se cargue correctamente desde el URL de la pagina
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Muy buen contenido')
        self.assertTemplateUsed(respuesta, 'inicio.html')

    def test_vista_detalle_publicacion(self):
        respuesta = self.client.get('/pub/1/')
        sin_respuesta = self.client.get('/pub/1000000/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(sin_respuesta.status_code, 404)
        self.assertContains(respuesta, 'Un buen titulo')
        self.assertTemplateUsed(respuesta, 'detalle_publicaciones.html')

    def test_vista_crear_publicacion(self):
        respuesta=self.client.post(reverse('nueva_publicacion'), {
        'titulo':'Nuevo título',
        'cuerpo':'Nuevo texto',
        'autor':self.user.id,
        })
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(Publicaciones.objects.last().titulo,'Nuevo título')
        self.assertEqual(Publicaciones.objects.last().cuerpo,'Nuevo texto')

    def test_vista_editar_publicacion(self):
        respuesta=self.client.post(reverse('editar_publicacion', args=1),
        {
            'titulo':'Titulo modificado',
            'cuerpo':'Cuerpo modificado',
        })
        self.assertEqual(respuesta.status_code,302)

    def test_vista_eliminar_publicacion(self):
        respuesta=self.client.post(reverse('eliminar_publicacion', args=1))
        self.assertEqual(respuesta.status_code,302)