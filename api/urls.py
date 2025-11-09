from django.urls import path
from .views import (
    HelloView,
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserProfileView
)

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
