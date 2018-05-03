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

def buses(request):
    return render(request, 'trippy/buses.html')

def rentals(request):
    return render(request, 'trippy/rentals.html')

def packages(request):
    return render(request, 'trippy/packages.html')
