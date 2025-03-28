from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import SearchRoomsForm
from datetime import datetime

def search_rooms(request):
    available_rooms = None
    if request.method == 'POST':
        form = SearchRoomsForm(request.POST)
        if form.is_valid():
            capacity = form.cleaned_data['capacity']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            available_rooms = Booking.available_rooms(capacity, start_time, end_time)
    else:
        form = SearchRoomsForm()
    return render(request, 'search_rooms.html', {'form': form, 'available_rooms': available_rooms})

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    if start_time and end_time:
        start_time = datetime.fromisoformat(start_time)
        end_time = datetime.fromisoformat(end_time)
        Booking.objects.create(user=request.user, room=room, start_time=start_time, end_time=end_time)
    return redirect('search_rooms')