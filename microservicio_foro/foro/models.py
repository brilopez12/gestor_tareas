from django.db import models

# Create your models here.
class Pregunta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    user_id = models.IntegerField()  # viene del microservicio Laravel
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name="respuestas", on_delete=models.CASCADE)
    contenido = models.TextField()
    user_id = models.IntegerField()  # viene del microservicio Laravel
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta a {self.pregunta.titulo}"