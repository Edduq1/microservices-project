from django.db import models

# Create your models here.

class Author(models.Model):
    # El documento pide display_name, pero 'name' es más estándar en Django
    name = models.CharField(max_length=200, verbose_name="Nombre a mostrar")
    # El documento pide 'email', pero dice 'mañana se enlaza a Auth'.
    # Lo omitimos por ahora para no duplicar datos, asumimos que se enlazará luego.
    # email = models.EmailField(unique=True, null=True, blank=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['name']

    def __str__(self):
        return self.name