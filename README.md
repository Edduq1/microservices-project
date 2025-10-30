# 📌 Resumen del Proyecto

Proyecto de microservicios con Docker, Django y React, organizado en servicios desacoplados para autenticación, contenido, notificaciones, frontend y proxy de enrutamiento. Servicios base: PostgreSQL y Redis.

Componentes:
- 🔐 `auth-service`: Autenticación de usuarios y emisión de tokens JWT.
- 📝 `blog-service`: Gestión de publicaciones, autores y categorías.
- ✉️ `email-service`: Envío de notificaciones y formularios.
- 🖥️ `frontend`: Interfaz de usuario en React.
- 🔀 `reverse-proxy`: Nginx como gateway y balanceador de carga local.
- 🐘 `PostgreSQL`: Base de datos relacional.
- 🧠 `Redis`: Caché en memoria y broker de mensajes.

---

## 📅 Día 1

### 🛠️ Actividades realizadas
- Configuración inicial del entorno con Docker y Docker Compose.
- Definición y levantamiento de contenedores para `PostgreSQL` y `Redis`.
- Preparación del `auth-service` con `Dockerfile` y `requirements.txt`.
- Creación de `test_connection.py` para verificar conectividad.
- Comprobación de conectividad desde `auth-service` hacia `PostgreSQL` y `Redis`.
- Organización de estructura de carpetas y archivos base del proyecto.

### 📁 Estructuras implementadas
```
microservices-project/
├── microservices-lab/
│   ├── auth-service/
│   │   ├── Dockerfile             # Receta para construir la imagen del servicio
│   │   ├── README.md
│   │   ├── requirements.txt       # Dependencias de Python
│   │   └── test_connection.py     # Script para verificar la conexión
│   ├── blog-service/
│   │   └── README.md
│   ├── email-service/
│   │   └── README.md
│   ├── frontend/
│   │   └── README.md
│   └── reverse-proxy/
│       └── README.md
├── .env.example                   # Plantilla de variables de entorno
├── .gitignore                     # Archivos ignorados por Git
├── docker-compose.yml             # Gestor de contenedores Docker
└── README.md                      # Documentación principal del proyecto
```

### 🔧 Comandos ejecutados
- Levantar servicios:
```bash
docker compose up -d
```
- Verificar contenedores activos:
```bash
docker ps
```
- Probar conectividad interna desde `auth-service`:
```bash
docker exec -it auth_service python test_connection.py
```

### ✅ Objetivos cumplidos
- Entorno base operativo con base de datos y caché.
- Conectividad comprobada entre `auth-service`, `PostgreSQL` y `Redis`.
- Estructura inicial de proyecto y servicios lista para desarrollo.

### 💻 Tecnologías utilizadas
- Docker, Docker Compose, PostgreSQL, Redis, Python.

---

## 📅 Día 2

### 🛠️ Actividades realizadas
- Transformación de `auth-service` en API REST con `Django` + `DRF` y `JWT`.
- Instalación de dependencias: `djangorestframework`, `djangorestframework-simplejwt`, `django-cors-headers`, `django-redis`, `gunicorn`.
- Creación del proyecto `core` y la aplicación `users`.
- Configuración de `PostgreSQL` y `Redis` en `settings.py`.
- Definición de `AUTH_USER_MODEL` y modelo de usuario personalizado (`UserManager`).
- Implementación de serializers y vistas (`RegisterView`, `MeView`).
- Definición de rutas (`users/urls.py`, `core/urls.py`).
- Aplicación de migraciones.
- Actualización de `Dockerfile` y configuración de `docker-compose.yml` (puerto `8000`, volúmenes y variables de entorno).
- Verificación de conexión a BD y caché desde shell de Django.

### 📁 Estructuras implementadas
```
auth-service/
├── core/                       # Proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Configuración principal de Django
│   ├── urls.py                 # URLs del proyecto
│   └── wsgi.py                 # Entrypoint para Gunicorn
├── users/                      # App de usuarios
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py               # Modelo User y UserManager
│   ├── tests.py
│   ├── urls.py                 # URLs de la app users
│   └── views.py                # Vistas (RegisterView, MeView) y Serializers
├── Dockerfile                  # Receta actualizada
├── manage.py                   # Utilidad de comandos de Django
├── README.md                   # Documentación del servicio
├── requirements.txt            # Dependencias de Python
└── test_connection.py          # Script de prueba (Día 1)
```

### 🔧 Comandos ejecutados
- Crear proyecto Django:
```bash
docker exec -it <contenedor_auth> startproject core .
```
- Crear aplicación `users`:
```bash
docker exec -it <contenedor_auth> startapp users
```
- Migraciones de base de datos:
```bash
docker exec -it <contenedor_auth> python manage.py makemigrations users
docker exec -it <contenedor_auth> python manage.py migrate
```

### 🧪 Validaciones realizadas en Postman
- `POST /api/register/`: Creación de nuevos usuarios.
- `POST /api/token/`: Obtención de tokens JWT (Login).
- `POST /api/token/refresh/`: Refresco del token de acceso.
- `GET /api/me/`: Información del usuario autenticado (requiere Bearer token).

### Endpoints API (auth-service) 📍
Estos son los endpoints implementados hasta ahora. Se pueden probar con herramientas como Postman.

- Registro de Usuario
  - `POST /api/register/`
  - Body (JSON):
```json
{
  "email": "usuario@ejemplo.com",
  "password": "password123"
}
```
  - Descripción: Crea un nuevo usuario en el sistema.

- Obtención de Tokens (Login)
  - `POST /api/token/`
  - Body (JSON):
```json
{
  "email": "usuario@ejemplo.com",
  "password": "password123"
}
```
  - Descripción: Autentica al usuario y devuelve un `access_token` (corta duración) y un `refresh_token` (larga duración).

- Refresco de Token
  - `POST /api/token/refresh/`
  - Body (JSON):
```json
{
  "refresh": "<refresh_token_obtenido_en_login>"
}
```
  - Descripción: Permite obtener un nuevo `access_token` usando un `refresh_token` válido.

- Obtener Datos del Usuario
  - `GET /api/me/`
  - Authorization: `Bearer <access_token_obtenido>` (enviar como cabecera `Authorization: Bearer TU_TOKEN`)
  - Descripción: Devuelve la información (`id`, `email`) del usuario autenticado asociado al `access_token`.

### Nota para Frontend: Manejo de Tokens JWT 💡
La autenticación de la API utiliza JSON Web Tokens (JWT) con un sistema de dos tokens para combinar seguridad con una buena experiencia de usuario:

- Access Token (🔑 Llave de Acceso Rápido)
  - Duración: Muy corta (ej., 5 minutos por defecto).
  - Uso: Se envía en la cabecera `Authorization` de cada petición a endpoints protegidos (ej., `/api/me/`) para identificarte.
  - Formato: `Authorization: Bearer <access_token>`. Es como una credencial temporal que usas constantemente.

- Refresh Token (🗝️ Llave Maestra)
  - Duración: Mucho más larga (ej., 1 día por defecto).
  - Uso: Su único propósito es obtener un nuevo `access_token` cuando el actual expire. Solo se envía al endpoint `/api/token/refresh/`. Es como una llave de respaldo que se usa raramente.

- Flujo Recomendado para Consumir la API
  - Este flujo está diseñado para que la corta duración del `access_token` sea prácticamente invisible para el usuario.
  - Login (`POST /api/token/`):
    - Envía `email` y `password` en el cuerpo (JSON).
    - Recibirás ambos tokens (`access` y `refresh`).
    - Guarda ambos de forma segura (ej., `localStorage`, `sessionStorage` o cookies HttpOnly para mayor seguridad).
  - Llamadas a Endpoints Protegidos (ej., `GET /api/me/`):
    - Incluye el `access_token` guardado en la cabecera: `Authorization: Bearer <access_token>`.
  - Manejo de Expiración del Access Token (`401 Unauthorized`):
    - Si una llamada a un endpoint protegido falla con un estado `401`, significa que tu `access_token` expiró.
    - No mandes al usuario a login todavía.
  - Refrescar el Access Token (Automáticamente):
    - Realiza una petición `POST` al endpoint `/api/token/refresh/`.
    - En el cuerpo (Body) de esta petición (tipo raw, JSON), envía el `refresh_token` que guardaste:
```json
{
  "refresh": "TU_REFRESH_TOKEN_GUARDADO"
}
```
  - Procesar Respuesta del Refresh:
    - Si tiene éxito: El backend responderá con un JSON que contiene un nuevo `access_token`.
    - Guarda este nuevo `access_token` (reemplazando el viejo expirado).
    - Vuelve a intentar la petición original (la que falló), pero ahora usando el nuevo `access_token` en la cabecera `Authorization`. El usuario ni se enterará. ✅
    - Si falla (`401 Unauthorized`): Esto significa que el `refresh_token` también ha expirado. La sesión del usuario ha terminado por completo.
    - Limpia cualquier token (`access` y `refresh`) guardado.
    - Redirige al usuario a la página de login. 🔄

### ✅ Objetivos cumplidos
- API de autenticación funcional con emisión y refresco de tokens JWT.
- Conexión estable con `PostgreSQL` y `Redis`.
- Endpoints disponibles para registro, login, refresco y perfil.

### 💻 Tecnologías utilizadas
- Django, Django REST Framework, Simple JWT, django-cors-headers, django-redis, Gunicorn, Docker, PostgreSQL, Redis.

---

---

## 📅 Día 3

### 🛠️ Actividades realizadas
- Se habilitó `blog-service` como API pública en `http://localhost:8001`.
- Conexión validada con `PostgreSQL` y `Redis` (caché para endpoints críticos).
- Se creó y documentó el script de semillas `seed_blog.py` para poblar datos.
- Se implementaron endpoints para categorías, posts (listado, búsqueda, detalle por `slug`) y healthcheck.
- Se configuró paginación (`PAGE_SIZE=10`) y búsqueda (`SearchFilter`) en posts.
- Se añadió caché con `django-redis` para respuestas de categorías (120s) y detalle de post (60s).
- (Opcional) Middleware de logger para inspeccionar el header `Authorization` en solicitudes.

### 📁 Estructura implementada (blog-service)
```
microservices-lab/blog-service/
├── authors/                     # App de autores
│   ├── __init__.py
│   ├── admin.py                 # Registro admin
│   ├── apps.py                  # Configuración de la app
│   ├── migrations/              # Migraciones de BD
│   │   ├── 0001_initial.py      # Modelo inicial Author
│   │   └── __init__.py
│   ├── models.py                # Modelo Author y relaciones
│   ├── serializers.py           # Serializer de Author
│   ├── tests.py
│   └── views.py                 # Vistas/Endpoints de Author
├── categories/                  # App de categorías
│   ├── __init__.py
│   ├── admin.py                 # Registro admin
│   ├── apps.py                  # Configuración de la app
│   ├── migrations/              # Migraciones de BD
│   │   ├── 0001_initial.py      # Modelo inicial Category
│   │   └── __init__.py
│   ├── models.py                # Modelo Category (slug, active)
│   ├── serializers.py           # Serializer de Category
│   ├── tests.py
│   ├── urls.py                  # Rutas /api/categories/
│   └── views.py                 # Listado con caché Redis (TTL 120s)
├── core/                        # Proyecto Django principal
│   ├── __init__.py
│   ├── asgi.py                  # Entrypoint ASGI
│   ├── middleware.py            # Logger opcional Authorization
│   ├── settings.py              # Configuración DB, Redis, DRF, paginación
│   ├── urls.py                  # Enrutamiento raíz (categories, posts, healthz)
│   └── wsgi.py                  # Entrypoint WSGI
├── posts/                       # App de publicaciones
│   ├── __init__.py
│   ├── admin.py                 # Registro admin
│   ├── apps.py                  # Configuración de la app
│   ├── management/              # Comandos Django
│   │   └── commands/
│   │       └── seed_blog.py     # Semillas: 30 posts, 5 categorías, 3 autores
│   ├── migrations/              # Migraciones de BD
│   │   ├── 0001_initial.py      # Modelo inicial Post
│   │   ├── 0002_post_excerpt.py # Campo excerpt agregado
│   │   └── __init__.py
│   ├── models.py                # Modelo Post y relaciones
│   ├── serializers.py           # Serializer con author y category anidados
│   ├── tests.py
│   ├── urls.py                  # Rutas /api/posts/ y /api/posts/{slug}/
│   └── views.py                 # Listado, búsqueda y detalle (caché 60s)
├── utils/                       # App de utilidades compartidas
│   ├── __init__.py
│   ├── admin.py                 # sin cambios relevantes
│   ├── apps.py                  # sin cambios relevantes
│   ├── migrations/              # sin cambios relevantes
│   │   └── __init__.py
│   ├── models.py                # sin cambios relevantes
│   ├── tests.py                 # sin cambios relevantes
│   ├── urls.py                  # sin cambios relevantes
│   └── views.py                 # sin cambios relevantes
├── Dockerfile                   # Imagen del servicio (Gunicorn + Django)
├── manage.py                    # Utilidad de comandos Django
├── openapi.yaml                 # Especificación de la API (referencia)
├── README.md                    # Documentación del microservicio Blog
└── requirements.txt             # Dependencias de Python del servicio
```

### 🚀 Cómo Ejecutar y Probar
- Comando para crear 30 posts, 5 categorias y 3 autores para la base de datos.
```bash
docker compose exec blog-service python manage.py seed_blog
```

- Levantar el servicio (reconstruye si es necesario):
```bash
docker compose up --build -d blog-service
```

- Preparar migraciones:
```bash
docker compose exec blog-service python manage.py makemigrations
```

- Ejecutar migraciones:
```bash
docker compose exec blog-service python manage.py migrate
```

- Poblar la base de datos con datos de prueba:
```bash
docker compose exec blog-service python manage.py seed_blog
```

### ⚡ Endpoints de la API (Día 3)

1) Healthcheck
- Método y URL: `GET http://localhost:8001/healthz/`
- Descripción: Verifica la conexión con la Base de Datos y Redis.
- Validación (Respuesta Esperada):
```json
{
  "status": "ok",
  "db": "ok",
  "redis": "ok"
}
```

2) Listar Categorías
- Método y URL: `GET http://localhost:8001/api/categories/`
- Descripción: Devuelve una lista de todas las categorías activas. Este endpoint usa caché con Redis (TTL 120s).
- Validación (Respuesta Esperada):
```json
[
  { "id": 1, "name": "NombreCategoria1", "slug": "nombrecategoria1" },
  { "id": 2, "name": "NombreCategoria2", "slug": "nombrecategoria2" }
]
```

3) Listar Posts (con paginación)
- Método y URL: `GET http://localhost:8001/api/posts/`
- Descripción: Devuelve una lista paginada (`PAGE_SIZE=10`) de posts publicados. Los campos `author` y `category` se devuelven como objetos anidados.
- Validación (Respuesta Esperada):
```json
{
  "count": 30,
  "next": "http://localhost:8001/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "...",
      "slug": "...",
      "excerpt": "...",
      "author": { "id": 1, "name": "..." },
      "category": { "id": 2, "name": "..." },
      "published_at": "2024-10-30T12:34:56Z"
    }
  ]
}
```

4) Buscar Posts
- Método y URL: `GET http://localhost:8001/api/posts/?search=palabra`
- Descripción: Busca la `palabra` en el `title` y `content` de los posts publicados.
- Validación (Respuesta Esperada):
```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    { "id": 10, "title": "Post con palabra", "slug": "post-con-palabra", "excerpt": "...", "author": { "id": 3, "name": "..." }, "category": { "id": 1, "name": "..." }, "published_at": "..." }
  ]
}
```

5) Detalle de Post (por Slug)
- Método y URL: `GET http://localhost:8001/api/posts/{slug}/` (ej. `http://localhost:8001/api/posts/mi-post-de-ejemplo/`)
- Descripción: Devuelve el detalle de un post específico usando su `slug`. Este endpoint usa caché con Redis (TTL 60s).
- Validación (Respuesta Esperada):
```json
{
  "id": 1,
  "title": "...",
  "slug": "mi-post-de-ejemplo",
  "excerpt": "...",
  "content": "...",
  "author": { "id": 1, "name": "..." },
  "category": { "id": 2, "name": "..." },
  "published_at": "2024-10-30T12:34:56Z",
  "views": 0
}
```

6) (Opcional) Middleware Logger
- Método y URL: `GET http://localhost:8001/api/posts/`
- Descripción: Prueba de que el middleware loguea los headers `Authorization`.
- Validación: Revisar los logs del contenedor y verificar el mensaje.
```bash
docker compose logs blog-service
```
Debe aparecer una línea similar a: `Authorization header found: Bearer <token>`.

### 🏛️ Pila Tecnológica (Día 3)
- Django REST Framework
- `django-filter` (para `SearchFilter` y filtrado de consultas)
- `django-redis` (caché de respuestas y sesiones)
- `Faker` (para generación de datos en `seed_blog.py`)
- Gunicorn (servidor WSGI en producción del contenedor)

### ✅ Objetivos cumplidos (Día 3)
 - `blog-service` operativo en `:8001` con endpoints clave y caché.
 - Endpoints realizados y verificados de manera exitosa.
 - Datos de prueba disponibles mediante `seed_blog.py`.
 - Paginación y búsqueda funcionales; detalle con caché.

## Contribución 🤝
- 💡 Se agradecen ideas y mejoras. Abre un issue para discutir cambios.
- 🔧 Envía pull requests con descripciones claras y pruebas cuando aplique.
- 📚 Mantén la consistencia del estilo y la estructura del proyecto.

## Licencia ©️
- 📄 Licencia: Por definir.