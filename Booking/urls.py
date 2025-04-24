from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_rooms, name='search_rooms'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),  # Add this line
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('bookings/', views.active_bookings, name='active_bookings')
]