from locust import HttpUser, task, between
import random

class ForoUser(HttpUser):
    # Simulamos algunos IDs de usuarios que ya existen en el microservicio Laravel
    user_ids = [1, 2, 3]

    @task(3)
    def listar_preguntas(self):
        """Obtiene todas las preguntas publicadas"""
        self.client.get("/api/preguntas/")

    @task(2)
    def listar_respuestas(self):
        """Obtiene todas las respuestas publicadas"""
        self.client.get("/api/respuestas/")

    @task(1)
    def ver_pregunta_especifica(self):
        """Consulta una pregunta individual"""
        pregunta_id = random.randint(1, 10)
        self.client.get(f"/api/preguntas/{pregunta_id}/")

    @task(1)
    def crear_pregunta(self):
        self.client.post("/api/preguntas/", json={
            "titulo": f"Pregunta de prueba {random.randint(100,999)}",
            "descripcion": "Esta es una pregunta generada automáticamente para pruebas de carga.",
            "user_id": random.choice(self.user_ids)
        })

    @task(1)
    def crear_respuesta(self):
        """Crea una nueva respuesta a una pregunta existente"""
        self.client.post("/api/respuestas/", json = {
            "pregunta": 1, 
            "contenido": "Respuesta automática de prueba.",
            "user_id": 5
        })

