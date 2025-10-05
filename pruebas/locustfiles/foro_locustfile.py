from locust import HttpUser, task, between
import random

class ForoUser(HttpUser):
    # Simulamos algunos IDs de usuarios que ya existen en el microservicio Laravel
    user_ids = [1, 2, 3]

    # ----------- TAREAS DE LECTURA (GET) -----------

    @task(3)
    def listar_preguntas(self):
        """Obtiene todas las preguntas publicadas"""
        self.client.get("/preguntas/")

    @task(2)
    def listar_respuestas(self):
        """Obtiene todas las respuestas publicadas"""
        self.client.get("/respuestas/")

    @task(1)
    def ver_pregunta_especifica(self):
        """Consulta una pregunta individual"""
        pregunta_id = random.randint(1, 10)
        self.client.get(f"/preguntas/{pregunta_id}/")

    # ----------- TAREAS DE ESCRITURA (POST) -----------

    @task(1)
    def crear_pregunta(self):
        self.client.post("/preguntas/", json={
            "titulo": f"Pregunta de prueba {random.randint(100,999)}",
            "descripcion": "Esta es una pregunta generada automáticamente para pruebas de carga.",
            "user_id": random.choice(self.user_ids)
        })

    @task(1)
    def crear_respuesta(self):
        """Crea una nueva respuesta a una pregunta existente"""
        data = {
            "pregunta": random.randint(1, 10),  # IDs de preguntas existentes
            "contenido": "Respuesta automática de prueba.",
            "user_id": random.choice(self.user_ids)
        }
        self.client.post("/respuestas/")
