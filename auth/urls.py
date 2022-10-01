from django.urls import path, include
from .views import CustomAuthToken

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view())
]