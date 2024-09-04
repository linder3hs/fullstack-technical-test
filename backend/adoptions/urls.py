from rest_framework.routers import DefaultRouter
from .views import AdoptionViewSet

router = DefaultRouter()

router.register(r'adoptions', AdoptionViewSet, basename='adoptions')

urlpatterns = router.urls
