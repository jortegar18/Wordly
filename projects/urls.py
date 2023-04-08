from django.urls import path, include
from projects.views import UserRegistrationView, UserLoginView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login')
]