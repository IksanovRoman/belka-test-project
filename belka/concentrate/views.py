from django.shortcuts import render

# Create your views here.
from rest_framework import generics
import django_filters.rest_framework

from concentrate.serializers import *


class ConcentrateAPIView(generics.ListCreateAPIView):
    queryset = Concentrate.objects.all()
    serializer_class = ConcentrateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['month']

class ConcentrateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Concentrate.objects.all()
    serializer_class = ConcentrateSerializer
