from django.urls import path
from . import views
from .views import RoomCreateView

urlpatterns = [
    path('search/', views.search_rooms, name='search_rooms'),
    path('room/<int:room_id>/', views.room_detail, name='room_detail'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
    path('bookings/', views.active_bookings, name='active_bookings'),
    path('pay/<int:room_id>/', views.pay_for_room, name='pay_for_room'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    path('new/', RoomCreateView.as_view(), name='room_create')
]