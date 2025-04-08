from django.shortcuts import render

def checkout_page(request):
    return render(request, 'checkout/chechout.html')


import stripe
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

def checkout_page(request):
    if request.method == 'POST':
       checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data' : {
                    'name': 'Room Booking',
                },
                'unit_amount': stripe_total,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('/success/')),
        cancel_url=request.build_absolute_uri(reverse('/cancel/')),
    
       ) 
    else:
        return render(request, 'checkout/checkout.html')

        def success_page(request):
            return render(request, 'checkout/success.html')

        def cancel_page(request):
            return render(request, 'checkout/cancel.html')
            

        
