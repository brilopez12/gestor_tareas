from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PreguntaViewSet, RespuestaViewSet

router = DefaultRouter()
router.register(r'preguntas', PreguntaViewSet)
router.register(r'respuestas', RespuestaViewSet)
urlpatterns = [
  path('',include(router.urls)),
]