from django.test import TestCase
from django.contrib.auth import get_user_model
from Booking.models import Room, Booking
from datetime import datetime, timedelta

class RoomModelTest(TestCase):
    def test_create_room(self):
        room = Room.objects.create(name="Test Room", capacity=10)
        self.assertEqual(room.name, "Test Room")
        self.assertEqual(room.capacity, 10)

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.room1 = Room.objects.create(name="Room 1", capacity=10)
        self.room2 = Room.objects.create(name="Room 2", capacity=5)

    def test_create_booking(self):
        booking = Booking.objects.create(user=self.user, room=self.room1, start_time=datetime.now(), end_time=datetime.now() + timedelta(hours=1))
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.room, self.room1)

    def test_available_rooms(self):
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=1)
        Booking.objects.create(user=self.user, room=self.room1, start_time=start_time, end_time=end_time)
        
        available_rooms = Booking.available_rooms(capacity=5, start_time=start_time, end_time=end_time)
        self.assertNotIn(self.room1, available_rooms)
        self.assertIn(self.room2, available_rooms)

# Run the tests using the following command in the terminal:
# python manage.py test Booking