from django.urls import path, include
from .views import ListUsers, URLShortner

urlpatterns = [
    path('users/', ListUsers.as_view()),
    path('url-shorten/', URLShortner.as_view()),
    path('arg2e.dom/<short_url>', URLShortner.as_view()),
]