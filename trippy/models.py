from django.db import models
from django.utils import timezone

# Create your models here.
class Location(models.Model):
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)
	Country = models.CharField(max_length=30)

class Accomodation(models.Model):
	HOTEL = 'HOT'
	INN = 'INN'
	HOSTEL = 'HOS'
	MOTEL = 'MOT'
	Accom_Type = [
		(HOTEL, 'Hotel'),
		(INN, 'Inn'),
		(HOSTEL, 'Hostel'),
		(MOTEL, 'Motel'),
	]
	Rate = models.DecimalField(max_digits=9, decimal_places=2)
	Discount = models.DecimalField(max_digits=2,decimal_places = 2)
	LocationId = models.ForeignKey('Location', on_delete=models.CASCADE)

class Transportation(models.Model):
	FLIGHT = 'FLI'
	CAR = 'CAR'
	CRUISE = 'CRU'
	Transport_Type = [
		(FLIGHT, 'Flight'),
		(CAR, 'Car Rental'),
		(CRUISE, 'Cruise'),
	]
	Date = models.DateField(default= timezone.now)
	SourceLocationId = models.ForeignKey('Location', on_delete=models.CASCADE,
		related_name='Src_%(class)s')
	DestLocationId = models.ForeignKey('Location', on_delete=models.CASCADE,related_name='Dest_%(class)s', default=0)

class Flight(models.Model):
	ONE_WAY = '1'
	ROUND_TRIP = '2'
	FLIGHT_TYPE_LIST = [
		(ONE_WAY, "One Way"),
		(ROUND_TRIP, "Round Trip")
	]

	FIRST = "FIR"
	BUSINESS = "BUS"
	ECONOMY = "ECO"
	FLIGHT_CLASS_LIST = [
		(FIRST, "First Class"),
		(BUSINESS, "Business Class"),
		(ECONOMY, 'Economy Class'),
	]
	NUM_TICKET_LIST = [
		('1', 1),
		('2', 2),
		('3', 3),
		('4', 4),
		('5', 5),
		('6', 6),
	]
	AIRPORT_LIST = [
		("JFK", "John F. Kennedy International Airport"),
		("PEK", "Beijing Capital International Airport"),
		("LAX", "Los Angeles International Airport"),
		("ICN", "Seoul Incheon International Airport"),
		("SIN", "Singapore Changi Airport")
	]
	FlightNumber = models.IntegerField()
	FlightCarrier = models.CharField(max_length=30)
	FlightPrice = models.DecimalField(max_digits=10, decimal_places=2)
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)


class CarRental(models.Model):
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)
	Rate = models.DecimalField(max_digits=10, decimal_places=2)
	CarType = models.CharField(max_length=30)

class Cruise(models.Model):
	NUM_TICKET_LIST = [
		('1', 1),
		('2', 2),
		('3', 3),
		('4', 4),
		('5', 5),
		('6', 6),
	]
	SOURCE_LOCATION_LIST = [
		("New-York", "New York"),
	]
	DEST_LOCATION_LIST = [
		("Bahamas", "Bahamas"),
		("Iceland", "Iceland"),
	]
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)
	CruisePrice = models.DecimalField(max_digits=10, decimal_places=2)
	CruiseNumber = models.IntegerField()

class Group(models.Model):
	size = models.IntegerField()

class Passenger(models.Model):
	GroupId = models.ForeignKey('Group', on_delete=models.CASCADE)
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	Email = models.EmailField()
	Gender = (
		("F", "Female"),
		("M", "Male"),
	)
	isLeader = models.BooleanField()


class Payment(models.Model):
	GroupLeaderId = models.ForeignKey('Passenger', on_delete = models.CASCADE)
	CardNumber = models.IntegerField()
	PaymentAmount = models.DecimalField(max_digits=10, decimal_places=2)
	CardExpiryDate = models.DateField()
