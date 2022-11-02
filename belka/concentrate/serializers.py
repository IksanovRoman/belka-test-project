from rest_framework import serializers

from concentrate.models import Concentrate, Month


class ConcentrateSerializer(serializers.ModelSerializer):
    month = serializers.SlugRelatedField(
        read_only=True,
        slug_field='month'
    )

    class Meta:
        model = Concentrate
        fields = ('id', 'name', 'iron', 'silicon', 'aluminum', 'calcium', 'sulfur', 'month')


class ConcentrateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concentrate
        fields = '__all__'

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'
