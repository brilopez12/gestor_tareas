# 📌 Microservicio de Tareas

Este microservicio gestiona las tareas del sistema: creación, actualización, consulta y eliminación.

## 🛠️ Tecnologías

* Framework: **Laravel**
* Base de datos: **MySQL**

## 📦 Requisitos

* PHP >= 8.x
* Composer
* MySQL

## ⚙️ Instalación

```bash
# Entrar al directorio del microservicio
cd microservicio_tareas

# Instalar dependencias
composer install

# Copiar archivo de entorno y configurar la conexión a MySQL
cp .env.example .env

# Generar la key de la aplicación
php artisan key:generate

# Ejecutar migraciones (solo crea la tabla de tareas)
php artisan migrate
```

## 🚀 Ejecución

```bash
php artisan serve
```

---