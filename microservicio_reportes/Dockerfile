# Imagen base
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONUNBUFFERED 1

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev && rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo
WORKDIR /var/www/html/microservicio_reportes

# Copiar requirements y luego instalar
COPY microservicio_reportes/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el proyecto entero
COPY microservicio_reportes/ .

# Exponer puerto
EXPOSE 5000

# Comando por defecto
CMD ["sh", "-c", "python wait_for_mysql.py && python app.py"]

