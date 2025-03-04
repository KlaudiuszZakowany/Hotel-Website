from django.urls import Path
from .views import request_service, service_list

urlpatterns = [
    path('request/', request_service, name = 'request_service'),
    path('list/', service_list, name = 'service_list'),
]