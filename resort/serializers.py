from rest_framework import serializers

from resort.models import Resort


class ResortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resort
        fields = '__all__'
