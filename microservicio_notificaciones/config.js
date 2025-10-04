import mysql from "mysql2/promise";

// Conexión a la DB de tareas
export const dbTareas = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "",   // agrega tu password si tienes
  database: "tareas"
});

// Conexión a la DB de seguridad (tabla: users)
export const dbSeguridad = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "",   // agrega tu password si tienes
  database: "seguridad"
});

// Configuración de Nodemailer con Hotmail/Outlook
export const MAIL_CONFIG = {
  host: "smtp.office365.com", // servidor SMTP de Outlook/Hotmail
  port: 587,                  // puerto TLS
  secure: false,              // debe ser false porque usamos STARTTLS
  auth: {
    user: "notificacionestarea360@hotmail.com", // tu correo
    pass: "Notificaciones360*"          // tu contraseña real
  },
  tls: {
    ciphers: "SSLv3"
  }
}