from django.db import models

class Room(models.Model):
    ROOM_TYPE = [
            ((1),("single")),
            ((2),("double")),
            ((3),("three")),
            ((4),("four"))
        ]

    room_number = models.IntegerField()
    floorNumber = models.IntegerField()
    room_price_night = models.FloatField() 
    room_type = models.CharField(max_length=10,choices=ROOM_TYPE)

    def __str__(self):
        return f"Room {self.room_number}, floor {self.floorNumber}, {self.room_type} bed(s)"
