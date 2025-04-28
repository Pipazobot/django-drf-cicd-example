from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AutorViewSet, LibroViewSet

router = DefaultRouter()
router.register(r"autores_bacanes", AutorViewSet)
router.register(r"libros_buenos", LibroViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
