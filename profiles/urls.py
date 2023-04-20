from django.urls import path, include
from knox import views as knox_views

from profiles.api import  updatePersonalDataTutor, updatePersonalDataStudent, CustomUserAPI

urlpatterns = [
    #path('api/profile/', getVolunteerRequests, name="volunteer_sessions"),
    path('api/profile/update_data_tutor', updatePersonalDataTutor, name="api_updateDataTutor"),
    path('api/profile/update_data_student', updatePersonalDataStudent, name="api_updateDataStudent"),
    path('api/profile/user_data', CustomUserAPI.as_view(), name='user_data'),
]