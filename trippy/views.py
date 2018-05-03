from django.shortcuts import render
from .forms import FlightForm

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
    return render(request, 'trippy/cruises.html')

def rentals(request):
    return render(request, 'trippy/rentals.html')

def packages(request):
    return render(request, 'trippy/packages.html')
