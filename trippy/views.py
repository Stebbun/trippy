from django.shortcuts import render
from .forms import FlightForm, CruiseForm, RegistrationForm, HotelForm


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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = RegistrationForm()
    return render(request, 'trippy/register.html', {'form' : form})
