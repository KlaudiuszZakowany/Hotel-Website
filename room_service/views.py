from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomService
from .forms import RoomServiceForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Booking.models import Booking
from django.utils.timezone import now

@login_required
def room_service(request):
    active_bookings = Booking.objects.filter(user=request.user, end_time__gte=now())
    return render(request, 'room_service.html', {'active_bookings': active_bookings})

def request_service(request):
    if request.method == "POST":
        form = RoomServiceForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('service_list')
    
    else:
        form = RoomServiceForm()
    return render(request, 'request_service.html', {'form' : form})

def service_list(request):
    services = RoomService.objects.all()
    return render(request, 'room_service/service_list.html', {'services' : services})

def service_detail(request, pk):
    service = get_object_or_404(RoomService, pk=pk)
    return render(request, 'room_service/service_detail.html.html', {'service': service})


        


