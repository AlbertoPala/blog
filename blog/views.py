from django.views.generic import ListView, DetailView
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
