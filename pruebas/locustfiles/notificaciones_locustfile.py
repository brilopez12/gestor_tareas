from locust import HttpUser, task

class NotificacionesUser(HttpUser):
    @task
    def notificar(self):
        # Endpoint del microservicio
        with self.client.get("/notificar", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Error {response.status_code}: {response.text}")
