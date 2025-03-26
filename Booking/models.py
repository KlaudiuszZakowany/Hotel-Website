from django.db import models
from django.conf import settings
from datetime import datetime  

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} (Capacity: {self.capacity})"

def get_default_room():
    room, created = Room.objects.get_or_create(name="Default Room", defaults={'capacity': 1})
    return room

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, default=get_default_room)
    start_time = models.DateTimeField(default=datetime.now,  blank=True)
    end_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.room.name} booked from {self.start_time} to {self.end_time}"

    @staticmethod
    def available_rooms(capacity, start_time, end_time):
        # Get all rooms that match the capacity requirement
        rooms = Room.objects.filter(capacity__gte=capacity)

        # Exclude rooms that are already booked in the given time range
        booked_rooms = Booking.objects.filter(
            start_time__lt=end_time,
            end_time__gt=start_time
        ).values_list('room', flat=True)

        return rooms.exclude(id__in=booked_rooms)