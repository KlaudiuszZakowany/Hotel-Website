from django.db import models

class Booking(models.Model):
    ROOM_CHOICES = [
            ('1', 'Single' ),
            ('2', 'Double' ),
            ('3', '1 Double 1 Single'),
            ('4' ,'4 Single'),
        ]

    checkin_date = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_nr = models.CharField(max_length=20)
    booking_email = models.EmailField()
    occupants = models.IntegerField()
    room_choice = models.CharField(max_length=50, choices=ROOM_CHOICES, default="1", null="1")

    def __str__(self):
        return f"Room {self.id}"
