from django.urls import URLPattern, path, include
from session.api import *

urlpatterns = [
    path('api/sessions/', get_sessions, name = "api_get_sessions"),
    path('api/my-sessions/tutors/', get_sessions_by_tutor, name = "api_get_my_sessions"),
    path('api/my-sessions/students/', get_sessions_by_student, name = "api_get_my_sessions"),
    path('api/sessions/create-session', insert_session, name = "api_insert_session"),
    path('api/sessions/session/<int:id>', get_session_by_id, name = "api_get_detail_session"),
    path('api/sessions/session/<int:id>/update', update_session, name = "api_update_session"),
    path('api/sessions/session/<int:id>/delete', delete_session, name = "api_delete_session"),
    #path('api/sessions/session/<int:id>/register-student', insert_student_in_session, name = "api_register_student"),
    path('api/sessions/session/get_requests', getVolunteerRequests, name="api_volunteer_requests"),
    path('api/sessions/session/<int:id>/create-turn', create_turn, name="api_create_turn"),
]