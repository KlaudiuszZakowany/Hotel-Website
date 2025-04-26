from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import SearchRoomsForm
from datetime import datetime, timedelta
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

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


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'room_detail.html', {'room': room})


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

@login_required
def active_bookings(request):
    bookings = Booking.objects.filter(user=request.user, end_time__gte=datetime.now())
    return render(request, 'active_bookings.html', {'bookings': bookings})

@login_required
def pay_for_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        if start_time and end_time:
            start_time = datetime.fromisoformat(start_time)
            end_time = datetime.fromisoformat(end_time)

            overlapping_bookings = Booking.objects.filter(
                room=room,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if overlapping_bookings.exists():
                return render(request, 'pay_for_room.html', {
                    'room': room,
                    'error': 'The room is not available for the selected dates. Please choose different dates.'
                })

            duration = (end_time - start_time).days
            if (end_time - start_time).seconds > 0:
                duration += 1

            total_price = room.price * duration

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': room.name,
                        },
                        'unit_amount': int(total_price * 100),  # Stripe expects the amount in cents
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/Booking/success/') + f'?room_id={room.id}&start_time={start_time}&end_time={end_time}',
                cancel_url=request.build_absolute_uri('/Booking/cancel/'),
            )
            return redirect(session.url, code=303)
    return render(request, 'pay_for_room.html', {'room': room})


@login_required
def payment_success(request):
    room_id = request.GET.get('room_id')
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    if not (room_id and start_time and end_time):
        return render(request, 'payment_error.html', {'error': 'Missing booking details.'})

    room = get_object_or_404(Room, id=room_id)
    Booking.objects.create(
        user=request.user,
        room=room,
        start_time=datetime.fromisoformat(start_time),
        end_time=datetime.fromisoformat(end_time),
    )

    return render(request, 'payment_success.html', {'room': room})

@login_required
def payment_cancel(request):
    return render(request, 'payment_cancel.html')