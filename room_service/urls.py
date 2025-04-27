from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.service_list, name = 'service_list'),
    path('<int:pk>/', views.service_detail, name = 'service_detail'),

]