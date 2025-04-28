from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Room, Booking
from datetime import datetime, timedelta

class BookingTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password123")
        
        self.room1 = Room.objects.create(name="Room 1", capacity=2, price=100.00)
        self.room2 = Room.objects.create(name="Room 2", capacity=4, price=200.00)
        
        self.booking1 = Booking.objects.create(
            user=self.user,
            room=self.room1,
            start_time=datetime.now() + timedelta(days=1),
            end_time=datetime.now() + timedelta(days=2)
        )
        self.booking2 = Booking.objects.create(
            user=self.user,
            room=self.room2,
            start_time=datetime.now() + timedelta(days=3),
            end_time=datetime.now() + timedelta(days=4)
        )

    def test_booking_creation(self):
        """Test that bookings are created correctly."""
        self.assertEqual(Booking.objects.count(), 2)
        self.assertEqual(self.booking1.room.name, "Room 1")
        self.assertEqual(self.booking2.room.capacity, 4)

    def test_booking_overlap(self):
        """Test that overlapping bookings are not allowed."""
        overlapping_booking = Booking.objects.filter(
            room=self.room1,
            start_time__lt=self.booking1.end_time,
            end_time__gt=self.booking1.start_time
        )
        self.assertTrue(overlapping_booking.exists())

    def test_available_rooms(self):
        """Test the available_rooms method."""
        start_time = datetime.now() + timedelta(days=5)
        end_time = datetime.now() + timedelta(days=6)
        available_rooms = Booking.available_rooms(2, start_time, end_time)
        self.assertIn(self.room1, available_rooms)
        self.assertIn(self.room2, available_rooms)

        start_time = datetime.now() + timedelta(days=1)
        end_time = datetime.now() + timedelta(days=2)
        available_rooms = Booking.available_rooms(2, start_time, end_time)
        self.assertNotIn(self.room1, available_rooms)
