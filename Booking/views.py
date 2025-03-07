from django.shortcuts import render, redirect

from .forms import InitialBookingForm

def get_booking(request):
    if request.method == "POST":
        form = InitialBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thankyou.html')
    
    else:
        form = InitialBookingForm()
    return render(request, 'booking.html', {'form' : form})

def thank_you(request):
    return render(request, 'thankyou.html')
