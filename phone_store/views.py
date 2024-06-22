from rest_framework import viewsets, permissions
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from .models import Marca, Celular, Especificaciones
from .serializer import MarcaSerializer, CelularSerializer, EspecificacionesSerializer

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class CelularViewSet(viewsets.ModelViewSet):
    serializer_class = CelularSerializer
    queryset = Celular.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class EspecificacionesViewSet(viewsets.ModelViewSet):
    serializer_class = EspecificacionesSerializer
    queryset = Especificaciones.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
