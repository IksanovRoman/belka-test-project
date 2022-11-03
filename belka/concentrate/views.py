from django.shortcuts import render

# Create your views here.
from rest_framework import generics
import django_filters.rest_framework
from django.db.models import *
from rest_framework.response import Response
from rest_framework.views import APIView

from concentrate.serializers import *


class ConcentrateAPIView(generics.ListCreateAPIView):
    queryset = Concentrate.objects.all()
    serializer_class = ConcentrateSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['month', 'iron']


class ConcentrateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Concentrate.objects.all()
    serializer_class = ConcentrateSerializer


class ReportAPIView(APIView):
    serializer_class = ConcentrateSerializer

    def get(self, request):
        month = request.GET.get("month")
        queryset = {}
        if month:
            month.capitalize()
            for x in ['iron', 'silicon', 'aluminum', 'calcium', 'sulfur']:
                queryset[x] = Concentrate.objects.filter(month=month).aggregate(максимум=Max(x), минимум=Min(x),
                                                                                среднее=Avg(x))

            return Response({'Железо': queryset.get('iron'), 'Кремний': queryset.get('silicon'),
                             'Алюминий': queryset.get('aluminum'), 'Кальций': queryset.get('calcium'),
                             'Сера': queryset.get('sulfur')})

        queryset = Concentrate.objects.all().values()
        return Response({'Все данные': queryset})
