from django.shortcuts import render

def checkout_page(request):
    return render(request, 'checkout/chechout.html')
    