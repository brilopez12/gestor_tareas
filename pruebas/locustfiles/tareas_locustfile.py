from locust import HttpUser, task
class SimpleUser(HttpUser):
    @task
    def index(self):
      self.client.get("/api/tasks")

    @task
    def create_task(self):
      self.client.post("/api/tasks", json={
            "userId": "2",
            "title": "Realizar el proyecto de software",
            "description": "Empezar por realizar 5 microservicios",
            "start_date": "2025-10-30",
            "end_date": "2025-11-02",
            "status": "Pendiente"
        })

    @task(1)
    def update_book(self):
        self.client.put("/api/task/1", json={
            "userId": "2",
            "title": "Realizar el proyecto de software II",
            "description": "Empezar por realizar 5 microservicios",
            "start_date": "2025-10-30",
            "end_date": "2025-11-02",
            "status": "Pendiente"
        })

    @task(1)
    def delete_book(self):
        self.client.delete("/api/task/2")
