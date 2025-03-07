from django.db import models

class Booking(models.Model):
    checkin_date = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_nr = models.IntegerField()
    booking_email = models.EmailField()
    occupants = models.IntegerField()
    checkin_date = models.DateField()
    room_number = models.IntegerField()
    room_price_night = models.FloatField() 

    def __str__(self):
        return f"Room {self.room_number}, floor {self.room_number}"
