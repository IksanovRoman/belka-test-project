from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, viewsets

from concentrate.models import Concentrate, Month
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

class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer
