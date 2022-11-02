from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from concentrate.models import Concentrate
from concentrate.serializers import *


class ConcentrateAPIView(generics.ListAPIView):
    queryset = Concentrate.objects.all()
    serializer_class = ConcentrateSerializer


class ConcentrateCreateAPIView(generics.CreateAPIView):
    queryset = Concentrate.objects.all()
    serializer_class = ConcentrateCreateSerializer


class ConcentrateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Concentrate.objects.all()
    serializer_class = ConcentrateCreateSerializer
