from django.test import TestCase
from .forms import InitialBookingForm

class BookingFormTestCase(TestCase):
    def test_valid_form(self):
        form = InitialBookingForm(data={'checkin_date': '2025-03-08', 
                                     'first_name': 'klaudiusz',
                                     'last_name': 'zakowany',
                                     'phone_nr': '0834638332',
                                     'booking_email': 'klaudiusz.zakowany@gmail.com', 
                                     'occupants': '6',
                                     'room_choice': '1',
                                     })
        self.assertTrue(form.is_valid())  # Form should be valid

    def test_invalid_form(self):
        form = InitialBookingForm(data={'checkin_date': '025-03-08', 
                                     'first_name': 'klaudiusz',
                                     'last_name': 'zakowany',
                                     'phone_nr': '0834638332',
                                     'booking_email': 'klaudiusz.zakowany@gmail.com', 
                                     'occupants': '6',
                                     'room_choice': '1',
                                     })
        self.assertFalse(form.is_valid())  # Form should be valid
