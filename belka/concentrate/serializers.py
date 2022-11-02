from rest_framework import serializers

from concentrate.models import Concentrate


class ConcentrateSerializer(serializers.ModelSerializer):
    month = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Concentrate
        fields = ('id', 'name', 'iron', 'silicon', 'aluminum', 'calcium', 'sulfur', 'month')


class ConcentrateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concentrate
        fields = '__all__'
