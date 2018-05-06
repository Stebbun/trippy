from django.db import models
from django.utils import timezone

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

# Create your models here.
class Location(models.Model):
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)
	Country = models.CharField(max_length=30)

	def __str__(self):
		return self.City

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
	NUM_ROOM_LIST = [
		('1', 1),
		('2', 2),
		('3', 3),
		('4', 4),
		('5', 5),
		('6', 6),
	]
	NUM_GUEST_LIST = [
		('1', 1),
		('2', 2),
		('3', 3),
		('4', 4),
		('5', 5),
		('6', 6),
		('7', 7),
		('8', 8),
		('9', 9),
		('10', 10),
		('11', 11),
		('12', 12),
	]
	LOCATION_LIST = [
		("New-York", "New York"),
		("Seattle", "Seattle"),
		("San-Francisco", "San-Francisco"),
	]
	Rate = models.DecimalField(max_digits=9, decimal_places=2)
	Discount = models.DecimalField(max_digits=2,decimal_places = 2)
	LocationId = models.ForeignKey('Location', on_delete=models.CASCADE)

class Transportation(models.Model):
	FLIGHT = 'FLI'
	CAR = 'CAR'
	CRUISE = 'CRU'
	Transport_Choices = [
		('Flight', 'Flight'),
		('Car', 'Car Rental'),
		('Cruise', 'Cruise'),
	]
	Transport_Type = models.CharField(max_length=10, choices=Transport_Choices, null=True)

	def __str__(self):
		return self.Transport_Type + " " + str(self.pk)

class Flight(models.Model):
	FlightNumber = models.CharField(max_length=10)
	FlightCarrier = models.CharField(max_length=30)
	FlightPrice = models.IntegerField()
	DepartureTime = models.DateTimeField(default=timezone.now)
	DepartureAirport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='Dest_%(class)s', default=0)
	ArrivalTime = models.DateTimeField(default=timezone.now)
	ArrivalAirport = models.ForeignKey('Airport', on_delete=models.CASCADE, default = 0)
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)

	def __str__(self):
		depart = str(self.DepartureTime.date()) + " " + str(self.DepartureTime.hour) + ":" + str(self.DepartureTime.minute)
		arrive = str(self.ArrivalTime.date()) + " " + str(self.ArrivalTime.hour) + ":" + str(self.ArrivalTime.minute)
		return str(self.DepartureAirport) + "[" + depart + "] to " + str(self.ArrivalAirport) + "[" + arrive + "]"

class CarRental(models.Model):
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)
	Rate = models.IntegerField()
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
	CruisePrice = models.IntegerField()
	CruiseNumber = models.IntegerField()

class Group(models.Model):
	size = models.IntegerField()

class Passenger(models.Model):
	GroupId = models.ForeignKey('Group', on_delete=models.CASCADE)
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	Email = models.EmailField()
	Gender = [
		("F", "Female"),
		("M", "Male"),
	]
	isLeader = models.BooleanField()

class Payment(models.Model):
	GroupLeaderId = models.ForeignKey('Passenger', on_delete = models.CASCADE)
	CardNumber = models.IntegerField()
	PaymentAmount = models.IntegerField()
	CardExpiryDate = models.DateField()

class Airport(models.Model):
	AirportCode = models.CharField(max_length=3)
	AirportName = models.CharField(max_length=100)
	LocationId = models.ForeignKey('Location', on_delete=models.CASCADE)

	def __str__(self):
		return self.AirportName + " (" + self.AirportCode +")"