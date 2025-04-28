from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.service_list, name = 'service_list'),
    path('room_service/<int:pk>/', views.service_detail, name = 'service_detail'),
    path('request-service/', views.request_service, name='request_service'),
    path('<int:pk>/', views.service_detail, name='service_detail'),

]