# 1. Usar imagen base Python 3.11 ligera
FROM python:3.11-slim

# 2. Establecer directorio de trabajo
WORKDIR /app

# 3. Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código (que crearemos después)
COPY . .

# 5. Comando temporal para mantener encendido mientras creamos archivos
CMD ["tail", "-f", "/dev/null"]