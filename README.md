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

## Contribución 🤝
- 💡 Se agradecen ideas y mejoras. Abre un issue para discutir cambios.
- 🔧 Envía pull requests con descripciones claras y pruebas cuando aplique.
- 📚 Mantén la consistencia del estilo y la estructura del proyecto.

## Licencia ©️
- 📄 Licencia: Por definir.