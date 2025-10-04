# 📌 Microservicio de Notificaciones de Tareas

Este microservicio se encarga de **notificar por correo electrónico** a los usuarios cuando sus tareas están próximas a vencer (2 días antes de la fecha de vencimiento).

---

## 🚀 Tecnologías utilizadas
- Node.js (v18+)
- Express
- MySQL
- Nodemailer

---

## ⚙️ Requisitos previos
1. Tener instalado **Node.js** y **npm**.
2. Tener configuradas las bases de datos MySQL:
   - Base de datos `tareas` con tabla `tareas`.
   - Base de datos `seguridad` con tabla `users`.
3. Una cuenta de correo gmail para enviar notificaciones.

---

## 📦 Instalación

Instalar dependencias:

```bash
cd microservicio-notificaciones
npm install
npm install express mysql2 nodemailer dotenv
```

---

## ▶️ Ejecución

Levantar el servidor:

```bash
node index.js
```

Por defecto corre en [http://localhost:3000](http://localhost:3000).


---