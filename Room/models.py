from django.db import models

class Room(models.Model):
    ROOM_TYPE = [
            ("single"),
            ("double"),
            ("three"),
            ("four")
        ]

    room_number = models.IntegerField(max_length=3)
    canTake = models.BooleanField(blank=True, null=True)
    floorNumber = models.IntegerField(max_length=5)
    room_price_night = models.FloatField(max_length=10) 
    room_type = models.CharField(choices=ROOM_TYPE)

    def __str__(self):
        return f"Room {self.room_number}, floor {self.floorNumber}, {self.room_type} bed(s)"
