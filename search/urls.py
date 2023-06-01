from django.urls import URLPattern, path, include
from search.api import *

urlpatterns = [
    #path('api/search/tutor/language', sessionCategory, name="api_sessions_by_category"),
    path('api/search/tutors/all', get_tutors, name="api_all_tutors"),
    path('api/search/tutors/language', tutors_by_language, name="get_tutors_by_language"),
    path('api/search/tutor', tutor_by_id, name="get_tutor_by_id"),
    path('api/search/tutor', student_by_id, name="get_tutor_by_id"),
    path('api/search/students/language', students_by_language, name="get_students_by_language")
]