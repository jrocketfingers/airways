from django.conf.urls import url, include
from rest_framework_nested import routers

from core.views import FlightViewSet, FlightUpdateViewSet

router = routers.DefaultRouter()
router.register(r'flights', FlightViewSet, base_name='flight')

flights_router = routers.NestedDefaultRouter(router, r'flights', lookup='flight')
flights_router.register(r'updates', FlightUpdateViewSet, base_name='flight-updates')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(flights_router.urls)),
]
