from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import FlightForm, CruiseForm, PaymentForm, HotelForm, PassengerForm, RentalForm, PackageForm
from .models import Airport, Flight, Passenger, Group, Location
import datetime

def strtoDate(string):
    string = string.split('-')
    return datetime.date(int(string[0]),int(string[1]),int(string[2]))

# Create your views here.
def index(request):
    return render(request, 'trippy/index.html')

def hotels(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            num_rooms=form['num_rooms'].data
            num_guests=form['num_guests'].data
            location = Location.objects.filter(pk= form['location'].data)[0]
            checkin = strtoDate(form['check_in_date'].data)
            checkout = strtoDate(form['check_out_date'].data)
            duration = (checkout-checkin).days
            link = '/information/?type=hotel&rooms='+num_rooms+"&guests="+num_guests+'&location='+str(location.pk)
            link += '&checkin='+str(form['check_in_date'].data)+'&checkout='+str(form['check_out_date'].data)
            link +='&duration='+str(duration)
            return redirect(link)
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
            if (form['flight_type'].data == "Round Trip"):
                retdate = "&retdate=" + str(form['return_date'].data)
            info = "&trip=" + str(form['flight_type'].data)
            info += '&class=' + str(form['flight_class'].data)+ '&tickets='+str(form['num_tickets'].data)
            src = '&src='+str(dairport.pk)+'&srcdate='+str(form['arrive_date'].data)
            dest = "&dest="+str(aairport.pk)
            link = '/information/?type=flight&to=true' + info + src + dest
            if retdate != None:
                link += retdate
            return redirect(link)
        else:
            errors_dict = form.errors.as_data()
            print(errors_dict)
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
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = RentalForm()
    return render(request, 'trippy/rentals.html', {'form' : form})

def packages(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = PackageForm()
    return render(request, 'trippy/packages.html', {'form' : form})

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
    if (request.GET.get('type') == 'flight'):
        trip = request.GET.get('trip')
        to = request.GET.get('to')
        toflight = request.GET.get('toflight')
        if toflight != None:
            toflight = int(toflight)
        fromflight = request.GET.get('fromflight')
        if fromflight != None:
            fromflight = int(fromflight)
        flight_class = request.GET.get('class')
        tickets = request.GET.get('tickets')
        src = int(request.GET.get('src'))
        srcName = Airport.objects.filter(id=src)[0]
        sdate = request.GET.get('srcdate')
        srcdate = sdate.split('-')
        dest = int(request.GET.get('dest'))
        destName = Airport.objects.filter(id=dest)[0]
        rdate = request.GET.get('retdate')
        retdate = None
        if rdate != None:
            retdate = rdate.split('-')
        dflights = Flight.objects.filter(DepartureAirport_id=src)
        dflights = dflights.filter(DepartureTime__contains=datetime.date(int(srcdate[0]), int(srcdate[1]), int(srcdate[2])))
        rflights = None
        if flight_class == 'First Class':
            classratio = int(tickets)*2
        elif flight_class == 'Business Class':
            classratio = float(tickets) * 1.5
        else:
            classratio = int(tickets)
        if dflights is None or len(dflights) == 0:
            dflights = None
        if retdate != None:
            rflights = Flight.objects.filter(ArrivalAirport_id=src)
            rflights = rflights.filter(ArrivalTime__contains=datetime.date(int(retdate[0]), int(retdate[1]), int(retdate[2])))
        if rflights is None or len(rflights) == 0:
            rflights = None
        context = { 'trip' : trip,
                    'to' : to,
                    'toflight' :toflight,
                    'fromflight' : fromflight,
                    'ticket_type' : flight_class,
                    'tickets' : tickets,
                    'classratio' : classratio,
                    'src' : src,
                    'srcName' : srcName,
                    'sdate' : sdate,
                    'dest' : dest,
                    'destName' : destName,
                    'rdate' : rdate,
                    'dflights' : dflights,
                    'rflights' : rflights }
    elif (request.GET.get('type') == 'hotel'):
        hotel = request.GET.get('type')
    return render(request, 'trippy/information.html', context)

def passenger(request):
    if request.method == 'POST':
        trip_type = request.GET.get('type')
        if trip_type == 'flight':
            trip = request.GET.get('trip')
            tickets = request.GET.get('tickets')
            flight_class = request.GET.get('class')
            toflight = request.GET.get('toflight')
            fromflight = request.GET.get('fromflight')
            num = int(request.GET.get('num'))
            form = PassengerForm(request.POST)
            if form.is_valid():
                if num == 1:
                    group = Group(size=int(tickets))
                    group.save()
                    group = group.pk
                else:
                    group = int(request.GET.get('groupid'))
                passenger = Passenger(FirstName=form['first_name'].data, LastName=form['last_name'].data, Email=form['email'].data, Gender=form['gender'].data, GroupId_id=group)
                passenger.save()
                if num == int(tickets):
                    link = '/payment/?type='+trip_type+'&trip='+trip+'&class='+flight_class+'&toflight='+toflight
                    if fromflight != None:
                        link += '&fromflight=' + fromflight
                    return redirect(link)
                    pass
                else:
                    num+=1
                    link = '/passenger/?type'+trip_type+'&trip='+trip+'&class='+flight_class+'&toflight='+toflight+'&num='+str(num)+'&groupid='+str(group)
                    if fromflight != None:
                        link += '&fromflight=' + fromflight
                    return redirect(link)
    else:
        form = PassengerForm()
    return render(request, 'trippy/passenger.html', {'form' : form})
