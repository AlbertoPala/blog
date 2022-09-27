from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    DeleteView
) #clases de edicion
from django.urls import reverse_lazy
from .models import Publicaciones

# Create your views here.
class VistaListaBlog(ListView):
    model = Publicaciones
    template_name = 'inicio.html'
    context_object_name = 'lista_publicaciones'
    
class VistaDetallePublicacion(DetailView):
    model = Publicaciones
    template_name = 'detalle_publicaciones.html'
    context_object_name = 'publicacion'

class VistaCrearBlog(CreateView):
    model = Publicaciones
    template_name = 'nueva_publicacion.html'
    fields = ['titulo', 'autor', 'cuerpo']
    
class VistaEditarBlog(UpdateView):
    model = Publicaciones
    template_name = 'editar_publicacion.html'
    fields = ['titulo', 'cuerpo']

class VistaEliminarBlog(DeleteView):
    model = Publicaciones
    template_name = 'eliminar_publicacion.html'
    context_object_name = 'publicacion'
    success_url = reverse_lazy('inicio')