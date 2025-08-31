from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegistrationView
from .token_views import CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='user_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]