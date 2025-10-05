from locust import HttpUser, task
class SimpleUser(HttpUser):

    @task
    def login(self):
        """Probar el login"""
        response = self.client.post("api/login", json={
            "email": "lopezbrigith90@gmail.com",     
            "password": "123456"    
        })
        if response.status_code == 200 and "access_token" in response.json():
            # guardar token para siguientes requests
            self.token = response.json()["access_token"]
            self.headers = {"Authorization": f"Bearer {self.token}"}
        else:
            self.token = None
            self.headers = {}

    @task
    def listar_usuarios(self):
        """GET /users"""
        if hasattr(self, "headers") and self.headers:
            self.client.get("api/users", headers=self.headers)

    @task
    def ver_usuario(self):
        """GET /users/1"""
        if hasattr(self, "headers") and self.headers:
            self.client.get("api/users/1", headers=self.headers)

    @task
    def logout(self):
        """Probar logout"""
        if hasattr(self, "headers") and self.headers:
            self.client.post("api/logout", headers=self.headers)
