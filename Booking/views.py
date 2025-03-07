from django.shortcuts import render, redirect

from .models import Booking
from .forms import InitialBookingForm

def request_service(request):
    if request.method == "POST":
        form = InitialBookingForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('service_list')
    
    else:
        form = InitialBookingForm()
    return request, 'room_service/request_service.html', {'form' : form}

def service_list(request):
    booking = Booking.objects.all()
    return request, 'room_service/service_list.html', {'services' : services}
        
