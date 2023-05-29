from django.urls import URLPattern, path, include
from availability.views import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'availability', AvailabilityViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
]