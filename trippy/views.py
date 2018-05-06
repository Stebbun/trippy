from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import FlightForm, CruiseForm, PaymentForm, HotelForm
from django.contrib import messages
from .models import Airport, Flight
import datetime


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
            aairport = Airport.objects.filter(AirportName = form['dest_location'].data)[0]
            retdate = None
            if (form['flight_type'].data == "One Way"):
                info = "?trip=one"
            else:
                info = "?trip=round"
                retdate = "&retdate=" + str(form['return_date'].data) 
            info += '&class=' + str(form['flight_class'].data)+ '&tickets='+str(form['num_tickets'].data) 
            src = '&src='+str(dairport.pk)+'&srcdate='+str(form['arrive_date'].data)
            dest = "&dest="+str(aairport.pk)
            link = '/information/' + info + src + dest
            if retdate != None:
                link += retdate
            return redirect(link)
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
    if request.GET.get('trip') == 'one':
        trip = 'One Way'
    else:
        trip = 'Round Trip'
    flight_class = request.GET.get('class')
    tickets = request.GET.get('tickets')
    src = int(request.GET.get('src'))
    srcName = Airport.objects.filter(id=src)[0]
    sdate = request.GET.get('srcdate')
    srcdate = sdate.split('-')
    dest = int(request.GET.get('dest'))
    destName = Airport.objects.filter(id=dest)[0]
    print(destName)
    rdate = request.GET.get('retdate')
    retdate = None
    if rdate != None:
        retdate = rdate.split('-')
    dflights = Flight.objects.filter(DepartureAirport_id=src)
    dflights = dflights.filter(DepartureTime__contains=datetime.date(int(srcdate[0]), int(srcdate[1]), int(srcdate[2])))
    rflights = None
    if retdate != None:
        rflights = Flight.objects.filter(ArrivalAirport_id=src)
        rflights = rflights.filter(ArrivalTime__contains=datetime.date(int(retdate[0]), int(retdate[1]), int(retdate[2])))
    context = { 'trip' : trip, 
                'ticket_type' : flight_class,
                'tickets' : tickets, 
                'srcName' : srcName,
                'sdate' : sdate,
                'destName' : destName,
                'rdate' : rdate,
                'dflights' : dflights,
                'rflights' : rflights }
    return render(request, 'trippy/information.html', context)
