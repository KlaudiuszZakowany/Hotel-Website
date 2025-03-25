from django.db import models

class checkout(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    room = models.CharField(max_length=1000)
    total_price = models.CharField(max_length=10000)
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')])

    def __str__(self):
        return f"{self.user} - {self.room} - {self.payment_status}"
        