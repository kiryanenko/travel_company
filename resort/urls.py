from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from resort.views import ResortViewSet

router = routers.DefaultRouter()
router.register(r'resorts', ResortViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
