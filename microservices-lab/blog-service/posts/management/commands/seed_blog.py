import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from categories.models import Category
from authors.models import Author
from posts.models import Post
from faker import Faker # Necesitarás añadir 'Faker' a requirements.txt

fake = Faker()

class Command(BaseCommand):
    help = 'Carga datos de ejemplo para el blog'

    def handle(self, *args, **kwargs):
        self.stdout.write("Eliminando datos antiguos...")
        Category.objects.all().delete()
        Author.objects.all().delete()
        Post.objects.all().delete()

        self.stdout.write("Creando categorías...")
        categories = []
        for i in range(5):
            name = fake.unique.word().capitalize()
            cat = Category.objects.create(name=name)
            categories.append(cat)
            self.stdout.write(f"- Creada categoría: {name}")

        self.stdout.write("Creando autores...")
        authors = []
        for i in range(3):
            name = fake.unique.name()
            auth = Author.objects.create(name=name)
            authors.append(auth)
            self.stdout.write(f"- Creado autor: {name}")

        self.stdout.write("Creando posts...")
        for i in range(30):
            title = fake.sentence(nb_words=6)
            status = random.choice(['draft', 'published'])
            post = Post.objects.create(
                title=title,
                content=fake.paragraph(nb_sentences=10),
                status=status,
                author=random.choice(authors),
                category=random.choice(categories)
            )
            self.stdout.write(f"- Creado post ({status}): {title[:30]}...")

        self.stdout.write(self.style.SUCCESS('¡Datos de ejemplo cargados exitosamente!'))