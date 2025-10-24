# 🔐 Auth Service

Servicio de autenticación y gestión de usuarios del proyecto de microservicios. Provee registro, login y autenticación basada en tokens JWT, conectándose a PostgreSQL y Redis.

---

## 🔐 Propósito General

Ser el corazón de la autenticación del sistema:
- Registrar y autenticar usuarios mediante email y contraseña.
- Emitir y validar tokens JWT (access y refresh).
- Exponer endpoints seguros para información del usuario autenticado.

---

## ✨ Funcionalidades Principales

- API REST para operaciones de autenticación y usuario.
- Autenticación JWT con doble token (access/refresh) para seguridad y renovación.
- Modelo de usuario personalizado basado en email (no username).
- Conexión a **PostgreSQL** (🐘) para persistencia y **Redis** (🧠) para caché/sesiones.

---

## 💻 Pila Tecnológica

- 🐍 Python
- 🚀 Django
- 🔧 Django REST Framework (DRF)
- 🔐 Simple JWT
- ⚡ Gunicorn
- 🐘 psycopg2-binary (PostgreSQL)
- 🧠 django-redis (Redis)

---

## 📁 Archivos Clave (descripción muy breve)

- `Dockerfile`: Definición del contenedor del servicio.
- `requirements.txt`: Dependencias de Python del servicio.
- `manage.py`: Utilidades de administración de Django.
- `core/`: Proyecto Django (configuración, rutas, WSGI).
- `users/`: Aplicación Django para modelo y endpoints de usuario.

---

## 🚀 Ejecución (mención breve)

Este servicio se levanta como parte del conjunto gestionado por `docker-compose` desde la raíz del proyecto:
- Iniciar todos los servicios: `docker compose up -d`.

> Para detalles de instalación, configuración y uso avanzado, consulta el `README.md` principal en la raíz del proyecto.