from django import forms


class InitialBookingForm(forms.ModelForm):
    checkin_date = forms.DateField(label="Date for check-in")
    occupants = forms.IntegerField(label="Occupants", max_value="6")

        