from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from hotel.views import HotelViewSet, OfferViewSet, TourViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'tours', TourViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
