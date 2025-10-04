# 📚 Microservicio de Foro de Ayuda (Django + MySQL)

---

## ⚙️ Tecnologías usadas

* **Python 3.10+**
* **Django 5.x**
* **Django REST Framework**
* **MySQL** como base de datos
* **mysqlclient** para la conexión a MySQL

---

## 📦 Instalación

1. **Iniciar el microservicio**

   ```bash
   cd microservicio_foro
   ```


2. **Instalar dependencias**

   ```bash
   pip install django djangorestframework mysqlclient
   ```

3. **Configurar la base de datos MySQL**
   Crea una base de datos llamada `foro`:


4. **Aplicar migraciones**

   ```bash
   python manage.py migrate
   ```

5. **Levantar el servidor con puerto 9000**

   ```bash
   python manage.py runserver 9000
   ```

   El servicio quedará corriendo en:
   👉 `http://localhost:9000`

---

## 🔌 Endpoints principales (API REST)

### Preguntas

* `GET api/preguntas/` → Lista todas las preguntas
* `POST api/preguntas/` → Crear nueva pregunta
* `GET api/preguntas/{id}/` → Ver detalle de una pregunta
* `PUT api/preguntas/{id}/` → Editar una pregunta
* `DELETE api/preguntas/{id}/` → Eliminar una pregunta

### Respuestas

* `GET api/respuestas/` → Lista todas las respuestas
* `POST api/respuestas/` → Crear nueva respuesta
* `GET api/respuestas/{id}/` → Ver detalle de una respuesta
* `PUT api/respuestas/{id}/` → Editar una respuesta
* `DELETE api/respuestas/{id}/` → Eliminar una respuesta


---