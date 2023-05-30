from django.urls import URLPattern, path, include
from availability.views import *

urlpatterns = [
    path('api/time-av/', get_time_av, name = "api_get_time-av"),
    path('api/my-time-av/', get_time_av_by_tutor, name = "api_get_my_time_av"),
    path('api/time-av/create', insert_time_av, name = "api_insert_time_av"),
    path('api/time-av/<int:id>/update', update_time_av, name = "api_update_time_av"),
    path('api/time-av/<int:id>/delete', delete_time_av, name = "api_delete_time_av"),

]