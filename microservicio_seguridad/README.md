# 🔐 Microservicio de Autenticación

Sistema de autenticación con **Laravel + Sanctum**.

## 🛠️ Tecnologías

* Framework: Laravel 
* Autenticación: Sanctum
* Base de datos: MySQL

## 📦 Requisitos

* PHP >= 8.1
* Composer
* MySQL

## ⚙️ Instalación

```bash
# Entrar al directorio
cd microservicio_autenticacion

# Instalar dependencias
composer install

# Configurar entorno
cp .env.example .env
php artisan key:generate

# Migraciones
php artisan migrate
```

## 🚀 Ejecución

```bash
php artisan serve
```

---