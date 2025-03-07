from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def Booking(request):
    return render(request, 'Booking.html')

def room_service(request):
    return render(request, 'room_service.html')