# Imagen base de Node.js
FROM node:20-slim

# Crear carpeta de trabajo
WORKDIR /var/www/html/microservicio_notificaciones

# Copiar package.json y package-lock.json
COPY microservicio_notificaciones/package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el proyecto
COPY microservicio_notificaciones/ .

# Exponer puerto
EXPOSE 3000

# Comando por defecto
CMD ["node", "index.js"]
