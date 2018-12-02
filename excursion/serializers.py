from rest_framework import serializers

from excursion.models import Excursion, ExcursionTour


class ExcursionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excursion
        fields = '__all__'


class ExcursionTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcursionTour
        fields = '__all__'
