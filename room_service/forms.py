from django import forms
from .models import RoomService

class RoomServiceForm(forms.ModelForm):
    class Meta:
        model = RoomService
        fields = [ 'room_number', 'service_choice', 'description']

        