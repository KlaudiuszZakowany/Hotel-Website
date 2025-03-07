from django.shortcuts import render, redirect

from .models import RoomService
from .forms import RoomServiceForm

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
    return render(request, 'service_list.html', {'services' : services})
        
