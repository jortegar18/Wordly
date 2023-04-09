from django.urls import path, include
from projects.views import UserRegistrationView, UserLoginView, UserProfileView, TutorRegistrationView, TutorLoginView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('register/tutor/', TutorRegistrationView.as_view(), name='tutor-register'),
    path('login/tutor/', TutorLoginView.as_view(), name='tutor-login'),
]