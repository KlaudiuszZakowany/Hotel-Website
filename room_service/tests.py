from django.test import TestCase
from .forms import RoomServiceForm

class RoomServiceFormTestCase(TestCase):
    def test_valid_form(self):
        form = RoomServiceForm(data={'room_number': '12', 
                                     'service_choice': 'laundry',
                                     'description': 'abc'
                                     })
        self.assertTrue(form.is_valid())  # Form should be valid

    def test_invalid_form(self):
        form = RoomServiceForm(data={'room_number': 'zzz', 
                                     'service_choice': 'buh',
                                     'description': 'a123'
                                     })
        self.assertFalse(form.is_valid())  # Form should be valid