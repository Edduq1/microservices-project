# 📝 Blog Service

Microservicio de contenido que expone API pública en `http://localhost:8001` para gestionar publicaciones (posts), autores y categorías.

## 📅 Día 3 (Resumen breve)
- Endpoints implementados: Healthcheck, listado de categorías, listado de posts (paginado y con búsqueda), y detalle de post por `slug`.
- Semillas de datos: `seed_blog` genera 30 posts, 5 categorías y 3 autores para pruebas.
- Caché: Respuestas de categorías (TTL 120s) y detalle de post (TTL 60s) usando Redis.
- DRF: Paginación (`PAGE_SIZE=10`) y búsqueda (`SearchFilter`).

## 🚀 Cómo ejecutar rápido
- Preparar datos de prueba (30 posts, 5 categorías y 3 autores):
```bash
docker compose exec blog-service python manage.py seed_blog
```
- Levantar servicio:
```bash
docker compose up --build -d blog-service
```
- Preparar migraciones:
```bash
docker compose exec blog-service python manage.py makemigrations
```
- Aplicar migraciones:
```bash
docker compose exec blog-service python manage.py migrate
```

## 📍 Endpoints clave
- `GET /healthz/`
- `GET /api/categories/`
- `GET /api/posts/`
- `GET /api/posts/?search=palabra`
- `GET /api/posts/{id}/`
- `GET /api/posts/{slug}/`

Tecnologías: Django REST Framework, `django-redis`, `django-filter`, `Faker`, Gunicorn.

Para más detalle (estructura y ejemplos), ver el README general en la raíz del proyecto.