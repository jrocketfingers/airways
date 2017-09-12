from rest_framework import routers

from core.views import FlightViewSet

router = routers.SimpleRouter()
router.register(r'flights', FlightViewSet, base_name='flight')
urlpatterns = router.urls
