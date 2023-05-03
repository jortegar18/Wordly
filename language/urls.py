from django.urls import URLPattern, path, include
from language.api import *

urlpatterns = [
    path('api/languages/', get_language, name = "api_get_alllanguages"),
    path('api/my-languages/', get_language_by_user, name = "api_get_my_language"),
    path('api/languages/create-language', insert_language, name = "api_insert_language"),
    path('api/languages/language/<int:id>/update', update_language, name = "api_update_language"),
    path('api/languages/language/<int:id>/delete', delete_language, name = "api_delete_language"),
    #path('api/workexp/language/<int:id>/register-volunteer', insert_volunteer_in_language, name = "api_register_volunteer"),
    #path('api/workexp/language/get_requests', getVolunteerRequests, name="api_volunteer_requests"),
    #path('api/workexp/language/<int:id>/create-turn', create_turn, name="api_create_turn"),
]