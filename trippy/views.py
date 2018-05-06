from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import FlightForm, CruiseForm, PaymentForm, HotelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Airport, Flight


# Create your views here.
def index(request):
    return render(request, 'trippy/index.html')

def hotels(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = HotelForm()
    return render(request, 'trippy/hotels.html', {'form' : form})

def flights(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            dairport = Airport.objects.filter(AirportName = form['source_location'].data)[0]
            dflights = Flight.objects.filter(DepartureAirport_id=dairport.pk).filter(DepartureTime__gte=form['arrive_date'].data)
            aairport = Airport.objects.filter(AirportName = form['dest_location'].data)[0]
            flights = dflights.filter(ArrivalAirport_id = aairport.pk).values()
            print(flights[0])
            return render(request, 'trippy/information.html', {'form': form, 'flights' : flights })
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
            pass
        else:
            form = PaymentForm()
    return render(request, 'trippy/payment.html', {'form' : form})

def information(request):
    return render(request, 'trippy/information.html')