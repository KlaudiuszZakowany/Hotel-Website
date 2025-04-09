from django.urls import path 
from .views import checkout_page
from . import views
urlpatterns = [
    path('', checkout_page, name='checkout'),
    path('', views.checkout_page, name='checkout'),
    path('success/', views.success_page, name='success'),
    path('cancel/', views.cancel_page, name='cancel'),

]