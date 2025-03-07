from django.db import models
from Room.models import Room

class Booking(models.Model):
    checkin_date = models.DateField()
    room_number = models.IntegerField()
    room_price_night = models.FloatField() 

    def __str__(self):
        return f"Room {self.room_number}, floor {self.floorNumber}, {self.room_type} bed(s)"
