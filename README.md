# Laboratorio de Microservicios (Django + React) 🧪

## Descripción 📝
Este repositorio contiene el código fuente para un proyecto de microservicios, diseñado para demostrar una arquitectura desacoplada y escalable utilizando Docker 🐳, Django 🐍 y React ⚛️.

### Arquitectura Final Planeada
La estructura del proyecto está dividida en los siguientes microservicios y componentes:

- 🔐 auth-service/ → Manejo de autenticación, usuarios y tokens JWT (Django).
- 📝 blog-service/ → Gestión de publicaciones, autores y categorías (Django).
- ✉️ email-service/ → Envío de notificaciones y gestión de formularios (Python/Flask).
- 🖥️ frontend/ → Interfaz de usuario construida con React.
- 🔀 reverse-proxy/ → Nginx como gateway y balanceador de carga local.

### Servicios Base
- 🐘 PostgreSQL: Base de datos relacional principal.
- 🧠 Redis: Caché en memoria y broker de mensajes.

## Instalación ⚙️
Día 1: Configuración del Entorno y Conectividad
En esta primera fase, se ha establecido la base del entorno de desarrollo con Docker. El objetivo fue configurar y levantar todos los servicios, asegurando que el microservicio de autenticación (auth-service) pudiera comunicarse correctamente con la base de datos y la caché.

### Arquitectura de Archivos (Día 1)
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
├── docker-compose.yml             # Gestor de los contenedores Docker
└── README.md                      # Documentación principal del proyecto
```

### ✅ Checklist de Avance (Día 1)
- [x] Estructura inicial del proyecto: Se crearon las carpetas para cada microservicio.
- [x] Configuración de .gitignore: Se añadió para excluir archivos sensibles.
- [x] Creación de .env.example: Se definió la plantilla para las variables de entorno.
- [x] Gestión con docker-compose.yml:
- [x] Se levantaron los contenedores de PostgreSQL y Redis.
- [x] Se añadió la configuración para construir y levantar el auth-service.
- [x] Configuración del auth-service:
- [x] Se creó el Dockerfile para definir la construcción de su imagen.
- [x] Se creó el requirements.txt con las dependencias necesarias.
- [x] Prueba de Conexión:
- [x] Se creó el script test_connection.py.
- [x] Se verificó exitosamente la conexión desde auth-service hacia PostgreSQL y Redis usando docker exec.

## Uso 🚀
Día 2: Implementación de Servicios (Próximamente)
- [ ] Desarrollo de la API REST en auth-service con Django.
- [ ] Creación de la aplicación base en frontend con React.

## Contribución 🤝
- 💡 Se agradecen ideas y mejoras. Abre un issue para discutir cambios.
- 🔧 Envía pull requests con descripciones claras y pruebas cuando aplique.
- 📚 Mantén la consistencia del estilo y la estructura del proyecto.

## Licencia ©️
- 📄 Licencia: Por definir.