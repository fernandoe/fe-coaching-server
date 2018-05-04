from rest_framework import routers

from .views import SessionModelViewSet

router = routers.SimpleRouter()
router.register(r'sessions', SessionModelViewSet)

urlpatterns = router.urls
