from django import forms
from .models import Booking

class InitialBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['checkin_date','first_name',
                  'last_name','phone_nr',
                  'booking_email','occupants',
                  'room_choice']


            