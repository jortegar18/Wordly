from django.urls import URLPattern, path, include
from workexp.api import *

urlpatterns = [
    path('api/workexp/', get_workexp, name = "api_get_workexp"),
    path('api/my-workexp/', get_workexp_by_tutor, name = "api_get_my_workexp"),
    path('api/workexp/create-workexp', insert_workexp, name = "api_insert_work_exp"),
    path('api/workexp/work_exp/<int:id>', get_workexp_by_id, name = "api_get_detail_work_exp"),
    path('api/workexp/work_exp/<int:id>/update', update_workexp, name = "api_update_work_exp"),
    path('api/workexp/work_exp/<int:id>/delete', delete_workexp, name = "api_delete_work_exp"),
    #path('api/workexp/work_exp/<int:id>/register-volunteer', insert_volunteer_in_work_exp, name = "api_register_volunteer"),
    #path('api/workexp/work_exp/get_requests', getVolunteerRequests, name="api_volunteer_requests"),
    #path('api/workexp/work_exp/<int:id>/create-turn', create_turn, name="api_create_turn"),
]