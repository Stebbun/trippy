from django.db import models
from django.utils import timezone

# Create your models here.
class Location(models.Model):
	City = models.CharField(max_length=30)
	State = models.CharField(max_length=30)
	Country = models.CharField(max_length=30)

	def __str__(self):
		return self.City+", " + self.State + ", " + self.Country

class Accomodation(models.Model):
	Accom_Type_Choices = [
		('Hotel', 'Hotel'),
		('Inn', 'Inn'),
		('Hostel', 'Hostel'),
		('Motel', 'Motel'),
	]
	AccomodationName = models.CharField(max_length=30, default=None)
	AccomodationType = models.CharField(max_length=5, choices=Accom_Type_Choices, default='Hotel')
	Rate = models.DecimalField(max_digits=9, decimal_places=2)
	Discount = models.DecimalField(max_digits=2,decimal_places = 2)
	LocationId = models.ForeignKey('Location', on_delete=models.CASCADE)

	def __str__(self):
		return self.AccomodationName

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
	ArrivalAirport = models.ForeignKey('Airport', on_delete=models.CASCADE, default=0)
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)

	def __str__(self):
		depart = str(self.DepartureTime.date()) + " " + str(self.DepartureTime.hour) + ":" + str(self.DepartureTime.minute)
		arrive = str(self.ArrivalTime.date()) + " " + str(self.ArrivalTime.hour) + ":" + str(self.ArrivalTime.minute)
		return str(self.DepartureAirport) + "[" + depart + "] to " + str(self.ArrivalAirport) + "[" + arrive + "]"

class CarRental(models.Model):
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)
	Rate = models.IntegerField()
	CarType = models.CharField(max_length=30)

'''
class Cruise(models.Model):
	CruisePrice = models.IntegerField()
	CruiseNumber = models.IntegerField()
	DepartureTime = models.DateTimeField(default=timezone.now)
	TransportId = models.OneToOneField('Transportation', primary_key=True, on_delete=models.CASCADE)
'''

class Group(models.Model):
	size = models.IntegerField()

class Passenger(models.Model):
	GroupId = models.ForeignKey('Group', on_delete=models.CASCADE)
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	Email = models.EmailField()
	Gender = models.CharField(max_length=1,choices=[
		("F", "Female"),
		("M", "Male"),
	], default='F')

	def __str__(self):
		return self.FirstName + self.LastName

class Payment(models.Model):
	GroupId = models.ForeignKey('Group', on_delete = models.CASCADE, default=0)
	CardNumber = models.CharField(max_length=16)
	PaymentAmount = models.IntegerField()
	CardExpiryDate = models.CharField(max_length=5)

	def __str__(self):
		return 'Group ' + str(self.GroupId.pk) + ' ('+ self.CardNumber[-4:] + " $" + str(self.PaymentAmount)+')'

class Airport(models.Model):
	AirportCode = models.CharField(max_length=3)
	AirportName = models.CharField(max_length=100)
	LocationId = models.ForeignKey('Location', on_delete=models.CASCADE)

	def __str__(self):
		return self.AirportName + " (" + self.AirportCode +")"

class CarRentalTime(models.Model):
	Car = models.ForeignKey('CarRental', on_delete = models.CASCADE)
	Driver = models.ForeignKey('Passenger', on_delete = models.CASCADE)
	StartRentalTime = models.DateField(default=timezone.now)
	EndRentalTime = models.DateField(default=timezone.now)
