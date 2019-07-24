##from django.shortcuts import render
# Create your views here.

from plants.models import Plant
from plants.serializers import PlantSerializer
from rest_framework import generics

class PlantListCreate(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer