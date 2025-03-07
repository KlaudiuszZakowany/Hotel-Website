from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_booking, name = 'get_booking'),
    path('ThankYou/', views.thank_you, name='thank_you'),
]