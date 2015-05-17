from django.views.generic import ListView, DetailView
from nomencladores.serializers import PersonaSerializer
from nomencladores.models import Persona
from rest_framework import viewsets

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

