from django.urls import path, include
from .views import request_service, service_list

urlpatterns = [
    path('request/', request_service, name = 'request_service'),
    path('list/', service_list, name = 'service_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
]