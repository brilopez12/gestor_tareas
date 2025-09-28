import express from "express";
import nodemailer from "nodemailer";
import { dbTareas, dbSeguridad, MAIL_CONFIG } from "./config.js";

const app = express();

// Transporter de correo
const transporter = nodemailer.createTransport(MAIL_CONFIG);

// Endpoint de notificación
app.get("/notificar", async (req, res) => {
  try {
    const [tareas] = await dbTareas.query(
      `SELECT id, title, end_date, userId
       FROM tasks
       WHERE end_date = CURDATE() + INTERVAL 2 DAY`
    );

    if (tareas.length === 0) {
      return res.json({ mensaje: "No hay tareas por vencer en 2 días" });
    }

    for (const tarea of tareas) {
      const [usuarios] = await dbSeguridad.query(
        "SELECT email, name FROM users WHERE id = ?",
        [tarea.usuario_id]
      );

      if (usuarios.length === 0) continue;
      const usuario = usuarios[0];

      const mailOptions = {
        from: MAIL_CONFIG.auth.user,
        to: usuario.email,
        subject: "📌 Recordatorio de tarea próxima a vencer",
        text: `Hola ${usuario.nombre},\n\nTu tarea "${tarea.titulo}" vence el ${tarea.fecha_vencimiento}.\n\n¡No olvides completarla!`
      };

      await transporter.sendMail(mailOptions);
      console.log(`Correo enviado a ${usuario.email} sobre la tarea: ${tarea.titulo}`);
    }

    res.json({ mensaje: "Notificaciones enviadas correctamente" });
  } catch (error) {
    console.error("Error en notificación:", error);
    res.status(500).json({ error: "Error al enviar notificaciones" });
  }
});

// Iniciar servidor
app.listen(3000, () => {
  console.log("Microservicio de notificaciones corriendo en http://localhost:3000");
});
