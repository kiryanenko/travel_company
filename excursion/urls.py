from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from excursion.views import ExcursionViewSet, ExcursionTourViewSet

router = routers.DefaultRouter()
router.register(r'excursions', ExcursionViewSet)
router.register(r'excursion_tours', ExcursionTourViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
