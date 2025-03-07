from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.request_service, name = 'request_service'),
    path('list/', views.service_list, name = 'service_list'),
]