# 1. Usar una imagen oficial de Python como base
FROM python:3.9-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias PRIMERO para aprovechar el caché de Docker
COPY requirements.txt .

# 4. Instalar todas las dependencias listadas en el archivo
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar todo el código de la aplicación al contenedor
COPY . .

# 6. Comando para mantener el contenedor corriendo (lo cambiaremos después)
CMD ["tail", "-f", "/dev/null"]