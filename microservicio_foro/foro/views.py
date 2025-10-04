from django.shortcuts import render
from .models import Pregunta, Respuesta
from rest_framework import viewsets, permissions
from .serializers import PreguntaSerializer, RespuestaSerializer


# Create your views here.
class PreguntaViewSet(viewsets.ModelViewSet):
  queryset = Pregunta.objects.all()

  serializer_class = PreguntaSerializer
  #Cualquiera puede ver preguntas y respuestas, solo registrados puede crear y responder para tener en cuenta a futuro
  '''def get_permissions(self):
        if self.action in ['list', 'retrieve']:  
            # cualquier persona puede ver
            permission_classes = [permissions.AllowAny]
        else:  
            # para crear/editar/eliminar, debe estar autenticado
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]'''

class RespuestaViewSet(viewsets.ModelViewSet):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer