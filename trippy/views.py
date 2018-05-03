from django.shortcuts import render
from .forms import FlightForm

# Create your views here.
def index(request):
    return render(request, 'trippy/index.html')

def flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = FlightForm()
    return render(request, 'trippy/flight.html', {'form' : form})
