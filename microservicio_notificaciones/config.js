import mysql from "mysql2/promise";

// Conexión a la DB de tareas
export const dbTareas = mysql.createPool({
  host: process.env.MYSQL_HOST_TAR,
  port: process.env.MYSQL_PORT_TAR,
  database: process.env.MYSQL_DATABASE_TAR,
  user: process.env.MYSQL_USER_TAR,
  password: process.env.MYSQL_PASSWORD_TAR
});

// Conexión a la DB de seguridad (tabla: users)
export const dbSeguridad = mysql.createPool({
  host: process.env.MYSQL_HOST_SEG,
  port: process.env.MYSQL_PORT_SEG,
  database: process.env.MYSQL_DATABASE_SEG,
  user: process.env.MYSQL_USER_SEG,
  password: process.env.MYSQL_PASSWORD_SEG
});

// Configuración de Nodemailer con Hotmail/Outlook
export const MAIL_CONFIG = {
  host: "smtp-relay.brevo.com", 
  port: 587,                 
  secure: false,            
  auth: {
    user: "988dd1001@smtp-brevo.com", 
    pass: "bdOcfZzIUptV2J8E"         
  },
  tls: {
    rejectUnauthorized: false
  }
}