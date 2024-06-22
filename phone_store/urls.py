from django.urls import include, path
from rest_framework import routers
from .views import MarcaViewSet, CelularViewSet, EspecificacionesViewSet

router = routers.DefaultRouter()
router.register(r'marca', MarcaViewSet)
router.register(r'celular', CelularViewSet)
router.register(r'especificaciones', EspecificacionesViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]