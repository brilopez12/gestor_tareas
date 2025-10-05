from locust import HttpUser, task, between
import random

class ReporteUser(HttpUser):

    estados = [None, "pendiente", "en_progreso", "completada"]
    formatos = ["json", "excel", "pdf"]

    @task(3)
    def obtener_reporte_json(self):
        """Prueba del endpoint en formato JSON (caso más frecuente)."""
        estado = random.choice(self.estados)
        params = {"formato": "json"}
        if estado:
            params["estado"] = estado
        self.client.get("/reporte/tareas", params=params, name="/reporte/tareas?formato=json")

    @task(1)
    def obtener_reporte_excel(self):
        """Prueba del endpoint generando un Excel."""
        estado = random.choice(self.estados)
        params = {"formato": "excel"}
        if estado:
            params["estado"] = estado
        self.client.get("/reporte/tareas", params=params, name="/reporte/tareas?formato=excel")

    @task(1)
    def obtener_reporte_pdf(self):
        """Prueba del endpoint generando un PDF."""
        estado = random.choice(self.estados)
        params = {"formato": "pdf"}
        if estado:
            params["estado"] = estado
        self.client.get("/reporte/tareas", params=params, name="/reporte/tareas?formato=pdf")
