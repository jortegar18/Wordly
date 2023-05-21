from django.urls import URLPattern, path, include
from payment.api import *

urlpatterns = [
    path('api/payment/', get_payment, name = "api_get_payment"),
    path('api/my-payments/', get_payment_by_user, name = "api_get_my_payment"),
    path('api/create-payment', insert_payment, name = "api_insert_payment"),
    path('api/payment/<int:id>', get_payment_by_id, name = "api_get_detail_payment"),
    path('api/payment/<int:id>/update', update_payment, name = "api_update_payment"),
    path('api/payment/<int:id>/delete', delete_payment, name = "api_delete_payment"),
    #path('api/payment/payment/<int:id>/register-volunteer', insert_volunteer_in_payment, name = "api_register_volunteer"),
    #path('api/payment/payment/get_requests', getVolunteerRequests, name="api_volunteer_requests"),
    #path('api/payment/payment/<int:id>/create-turn', create_turn, name="api_create_turn"),
]