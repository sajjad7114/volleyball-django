from django.urls import path
from rest_framework import routers
from .views import StadiumViewSet, MatchViewSet, TransActionAPIView, TransActionDetails, TicketAPIView, RetrieveTicket

router = routers.SimpleRouter()
router.register('match', MatchViewSet, basename='match')
router.register('stadium', StadiumViewSet, basename='stadium')

urlpatterns = [
    path('transaction/<int:uid>', TransActionAPIView.as_view()),
    path('transaction/<int:uid>/<int:pk>', TransActionDetails.as_view()),
    path('ticket/<int:uid>', TicketAPIView.as_view()),
    path('ticket/<int:uid>/<int:pk>', RetrieveTicket.as_view()),
]

urlpatterns += router.urls
