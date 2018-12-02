from rest_framework import viewsets

from resort.models import Resort
from resort.serializers import ResortSerializer


class ResortViewSet(viewsets.ModelViewSet):
    queryset = Resort.objects.all()
    serializer_class = ResortSerializer
