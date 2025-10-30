from django.db import models

# Create your models here.
from django.utils.text import slugify
from django.utils import timezone
# Importa los modelos relacionados
from categories.models import Category
from authors.models import Author

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    )

    title = models.CharField(max_length=255, verbose_name="Título")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Dejar en blanco para autogenerar.")
    # El documento dice 'body', pero 'content' es más común
    content = models.TextField(verbose_name="Contenido")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de publicación")
    # El documento menciona 'views', lo añadimos como un contador simple
    views = models.PositiveIntegerField(default=0, verbose_name="Vistas")

    # Relaciones
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts', verbose_name="Autor")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts', verbose_name="Categoría")

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        ordering = ['-published_at', '-created_at'] # Ordenar por fecha de publicación/creación

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # Si se marca como publicado y no tiene fecha, se pone la actual
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)