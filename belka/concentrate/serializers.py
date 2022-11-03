from rest_framework import serializers

from concentrate.models import Concentrate


class ConcentrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concentrate
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concentrate
        fields = "__all__"
