from django.shortcuts import render, redirect
from .forms import FlightForm, CruiseForm, PaymentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.
def index(request):
    return render(request, 'trippy/index.html')

def hotels(request):
    return render(request, 'trippy/hotels.html')

def flights(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = FlightForm()
    return render(request, 'trippy/flights.html', {'form' : form})

def cruises(request):
    if request.method == 'POST':
        form = CruiseForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CruiseForm()
    return render(request, 'trippy/cruises.html', {'form' : form})

def rentals(request):
    return render(request, 'trippy/rentals.html')

def packages(request):
    return render(request, 'trippy/packages.html')

def payment(request):
    form = PaymentForm(request.POST or None)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            print("valid")
        else:
            form = PaymentForm()
    return render(request, 'trippy/payment.html', {'form' : form})
