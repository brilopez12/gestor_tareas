import mysql from "mysql2/promise";

// Conexión a la DB de tareas
export const dbTareas = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "",   
  database: "tareas"
});

// Conexión a la DB de seguridad (tabla: users)
export const dbSeguridad = mysql.createPool({
  host: "localhost",
  user: "root",
  password: "",   
  database: "seguridad"
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