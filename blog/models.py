from django.db import models

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE
    )
    cuerpo = models.TextField()

    def __str__(self): #imprimir el objeto de la "publicacion" de la propiedad "titulo"
        return self.titulo

    #define como es la tabla, makegritations genera el codigo sql, se ejecuta ese codigo con migrate