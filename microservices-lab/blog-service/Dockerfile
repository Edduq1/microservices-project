# 1. Usar imagen base Python 3.11 ligera
FROM python:3.11-slim

# 2. Establecer directorio de trabajo
WORKDIR /app

# 3. Copiar e instalar dependencias
COPY requirements.txt .

# 4. Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código (que crearemos después)
COPY . .

# 5. Comando final para ejecutar el servidor Gunicorn en el puerto 8001
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8001"]