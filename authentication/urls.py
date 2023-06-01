from django.urls import path, include
from .api import RegisterTutorAPI, TutorAPI, LoginAPI, StudentAPI,  RegisterStudentAPI   
from knox import views as knox_views 

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register_tutor', RegisterTutorAPI.as_view()),
    path('api/auth/register_student', RegisterStudentAPI.as_view()),
    path('api/auth/tutor', TutorAPI.as_view()),
    path('api/auth/student', StudentAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),

]