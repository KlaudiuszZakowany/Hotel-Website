from django.urls import path
from . import views

urlpatterns = [
    path('search_rooms/', views.search_rooms, name='search_rooms'),
    path('book_room/<int:room_id>/', views.book_room, name='book_room'),
]