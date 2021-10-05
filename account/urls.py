from django.urls import path
from .views import UserViewSets
from rest_framework.authtoken import views

urlpatterns = [
    path('register', UserViewSets.as_view()),
    path('login', views.obtain_auth_token, name='login'),
]
