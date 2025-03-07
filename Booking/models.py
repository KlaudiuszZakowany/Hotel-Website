from django.db import models
from Room.models import Room

class Booking(models.Model):
    ROOM_TYPE = [
            ("single"),
            ("double"),
            ("three"),
            ("four")
        ]
    
    checkin_date = models.DateField()
    room_number = models.IntegerField(max_length=3)
    room_price_night = models.FloatField(max_length=10) 
    room_type = models.CharField(choices=ROOM_TYPE)

    def __str__(self):
        return f"Room {self.room_number}, floor {self.floorNumber}, {self.room_type} bed(s)"

class prefRoom(models.Model):

    occupancy = 0;