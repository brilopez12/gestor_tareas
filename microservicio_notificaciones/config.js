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

// Configuración de Nodemailer
export const MAIL_CONFIG = {
  service: "gmail",
  auth: {
    user: "soportereportes676@gmail.com",
    pass: "Soporte1234*"
  }
};
