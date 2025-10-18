# Descripción de la carpeta

- Propósito: Microservicio de autenticación y gestión de usuarios/sesiones. Actualmente orientado a validar la conectividad con servicios de infraestructura.
- Contenido:
  - `Dockerfile`: Imagen base `python:3.9-slim`, instala dependencias y prepara el contenedor.
  - `requirements.txt`: Dependencias (`psycopg2-binary`, `redis`) para conectar con PostgreSQL y Redis.
  - `test_connection.py`: Script que prueba conexión a PostgreSQL y Redis usando variables de entorno.
  - `README.md`: Este archivo.