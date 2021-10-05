from django.urls import path, include
from rest_framework import routers
from .views import StadiumViewSet, MatchViewSet

router = routers.SimpleRouter()
router.register('match', MatchViewSet, basename='match')
router.register('stadium', StadiumViewSet, basename='stadium')


urlpatterns = router.urls
