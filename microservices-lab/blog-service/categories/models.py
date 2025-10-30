from django.db import models

# Create your models here.
from django.utils.text import slugify # Para generar el slug automáticamente

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True, blank=True, help_text="Dejar en blanco para autogenerar.")
    is_active = models.BooleanField(default=True, verbose_name="¿Activa?")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name'] # Ordenar alfabéticamente por defecto

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Genera el slug automáticamente si está vacío
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)