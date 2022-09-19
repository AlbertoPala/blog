#blog

from django.urls import path
from .views import VistaDetallePublicacion, VistaListaBlog

urlpatterns = [
    path('', VistaListaBlog.as_view(), name='inicio'),
    path('pub/<int:pk>/', VistaDetallePublicacion.as_view(), name='detalle_pub'),
]