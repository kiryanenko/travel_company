from rest_framework import viewsets

from excursion.models import Excursion, ExcursionTour
from excursion.serializers import ExcursionSerializer, ExcursionTourSerializer


class ExcursionViewSet(viewsets.ModelViewSet):
    queryset = Excursion.objects.all()
    serializer_class = ExcursionSerializer


class ExcursionTourViewSet(viewsets.ModelViewSet):
    queryset = ExcursionTour.objects.all()
    serializer_class = ExcursionTourSerializer
