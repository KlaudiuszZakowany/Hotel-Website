from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomService
from .forms import RoomServiceForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Booking.models import Booking
from django.utils.timezone import now


def request_service(request):
    if request.method == "POST":
        form = RoomServiceForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('service_detail')
    
    else:
        form = RoomServiceForm()
    return render(request, 'request_service.html', {'form' : form})

def service_list(request):
    services = RoomService.objects.all()
    return render(request, 'service_list.html', {'services' : services})

def service_detail(request, pk):
    service = get_object_or_404(RoomService, pk=pk)
    return render(request, 'room_service/service_detail.html', {'service': service})

def request_services(request):
    if request.method == 'POST':
        service = Service.objects.create(
            room_number=request.POST['room_number'],
            service_choices=request.POST['service_choice'],
            description=request.POST.get('description', ''),
            price=request.POST.get('price', 0.00)
        )
        return redirect('service_deatil', pk=service.pk)
    else:
        return render(request, 'room_service/request_service.html')
        


