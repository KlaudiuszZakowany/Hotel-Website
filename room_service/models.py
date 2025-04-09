from django.db import models

class RoomService(models.Model):
    SERVICE_CHOICES = [
        ('extra_pillows', 'Extra Pillows and Blankets' ),
        ('laundry', 'Laundry' ),
        ('cleaning', 'Cleaning'),
        ('food' ,'Food'),
        ('special_requests', 'Special Requests'),
    ]

    room_number = models.CharField(max_length=10)
    service_choice = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='room_service_images/', blank=True, null=True)
    

    def __str__(self):
        return f"Room {self.room_number}, {self.service_choice}, {self.description}"
