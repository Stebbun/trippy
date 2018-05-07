from datetime import datetime, date, timedelta
from django.utils import timezone
from django import forms
from .models import Flight, Cruise, Payment, Passenger, Accomodation, Airport, Location
from django.core import validators

class FlightForm(forms.Form):
    flight_type = forms.ChoiceField(choices=[
        ('One Way', "One Way"),
        ('Round Trip', "Round Trip")
    ])
    flight_class = forms.ChoiceField(choices=[
        ("First Class", "First Class"),
        ("Business Class", "Business Class"),
        ("Economy Class", 'Economy Class'),
    ])
    num_tickets = forms.ChoiceField(choices=[
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
    ])
    source_location = forms.ModelChoiceField(queryset = Airport.objects.all(), empty_label=None, to_field_name="AirportName")
    dest_location = forms.ModelChoiceField(queryset = Airport.objects.all(), empty_label=None, to_field_name="AirportName")
    arrive_date = forms.DateField(initial=timezone.now)
    return_date = forms.DateField(initial=datetime.now() + timedelta(days=5))

    def clean(self):
        cleaned_data = super(FlightForm, self).clean()
        flight_type = cleaned_data.get('flight_type')
        num_tickets = cleaned_data.get('num_tickets')
        flight_class = cleaned_data.get('flight_class')
        source_location = cleaned_data.get('source_location')
        dest_location = cleaned_data.get('dest_location')
        arrive_date = cleaned_data.get('arrive_date')
        return_date = cleaned_data.get('return_date')
        if not (flight_type or num_tickets or flight_class
                or source_location or dest_location or arrive_date
                or return_date):
            raise forms.ValidationError('Invalid value', code='invalid')
        if source_location == dest_location:
            raise forms.ValidationError('Source and Destination must be different', code='invalid')
        if arrive_date >= return_date:
            raise forms.ValidationError('You must choose a date later than the departure date')

    def result(self):
        return [self['source_location']]

class HotelForm(forms.Form):
    num_rooms = forms.ChoiceField(label="Rooms", choices=[
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
    ])
    num_guests = forms.ChoiceField(label="Guests", choices=[
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
    ])
    location = forms.ModelChoiceField(queryset = Location.objects.all(), empty_label=None)
    check_in_date = forms.DateField(label="Check-In Date", initial=datetime.now())
    check_out_date = forms.DateField(label="Check-Out Date", initial=datetime.now())

    def clean(self):
        cleaned_data = super(HotelForm, self).clean()
        num_rooms = cleaned_data.get('num_rooms')
        num_guests = cleaned_data.get('num_guests')
        location = cleaned_data.get('location')
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')
        if not (num_rooms or num_guests or location or check_in_date
                or check_out_date):
            raise forms.ValidationError('Invalid input')

class CruiseForm(forms.Form):
    num_tickets = forms.ChoiceField(choices=[
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
    ])
    source_location = forms.ModelChoiceField(queryset = Location.objects.all(), empty_label=None, to_field_name="State")
    dest_location = forms.ModelChoiceField(queryset = Location.objects.all(), empty_label=None, to_field_name="State")
    arrive_date = forms.DateField(initial=datetime.now())
    return_date = forms.DateField(initial=datetime.now() + timedelta(days=1))

    def clean(self):
        cleaned_data = super(CruiseForm, self).clean()
        num_tickets = cleaned_data.get('num_tickets')
        source_location = cleaned_data.get('source_location')
        dest_location = cleaned_data.get('dest_location')
        arrive_date = cleaned_data.get('arrive_date')
        return_date = cleaned_data.get('return_date')
        if not (num_tickets or source_location or dest_location
                or arrive_date or return_date):
            raise forms.ValidationError('Invalid input')
        if source_location == dest_location:
            raise forms.ValidationError('Source and Destination must be different', code='invalid')

class RentalForm(forms.Form):
    pickup_location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label=None)
    dropoff_location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label=None)
    pickup_date = forms.DateField(initial=datetime.now())
    arrive_date = forms.DateField(initial=datetime.now() + timedelta(days=1))

    def clean(self):
        cleaned_data = super(RentalForm, self).clean()
        pickup_location = cleaned_data.get('pickup_location')
        dropoff_location = cleaned_data.get('dropoff_location')
        pickup_date = cleaned_data.get('pickup_date')
        arrive_date = cleaned_data.get('arrive_date')

class PackageForm(forms.Form):
    source_location = forms.ModelChoiceField(queryset = Airport.objects.all(), empty_label=None, to_field_name="AirportName")
    dest_location = forms.ModelChoiceField(queryset = Airport.objects.all(), empty_label=None, to_field_name="AirportName")
    arrive_date = forms.DateField(initial=timezone.now)
    return_date = forms.DateField(initial=datetime.now() + timedelta(days=5))
    hotel_location = forms.ModelChoiceField(queryset = Location.objects.all(), empty_label=None)
    check_in_date = forms.DateField(label="Check-In Date", initial=datetime.now())
    check_out_date = forms.DateField(label="Check-Out Date", initial=datetime.now())

    def clean(self):
        cleaned_data = super(PackageForm, self).clean()
        source_location = cleaned_data.get('source_location')
        dest_location = cleaned_data.get('dest_location')
        arrive_date = cleaned_data.get('arrive_date')
        return_date = cleaned_data.get('return_date')
        hotel_location = cleaned_data.get('hotel_location')
        check_in_date = cleaned_data.get('check_in_date')
        check_out_date = cleaned_data.get('check_out_date')

class BasePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields=["CardNumber", "PaymentAmount", "CardExpiryDate"]

class PaymentForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta(BasePaymentForm.Meta):
        fields = ['first_name','last_name','email'] + BasePaymentForm.Meta.fields

    def clean(self):
        cleaned_data = super(PaymentForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        card_number = cleaned_data.get('CardNumber')
        payment_amount = cleaned_data.get("PaymentAmount")
        expiry_date = cleaned_data.get('CardExpiryDate')
        if not (first_name or last_name or email or card_number
                or payment_amount or expiry_date):
            raise forms.ValidationError('Invalid input')

class PassengerForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ])

    def clean(self):
        cleaned_data = super(PassengerForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        gender = cleaned_data.get('gender')
        if not (first_name or last_name or email or gender):
            raise forms.ValidationError('Invalid input')
