import datetime
from django import forms
from .models import Flight, Cruise, Passenger, Accomodation
from django.core import validators

class FlightForm(forms.Form):
    flight_type = forms.ChoiceField(choices=Flight.FLIGHT_TYPE_LIST)
    flight_class = forms.ChoiceField(choices=Flight.FLIGHT_CLASS_LIST)
    num_tickets = forms.ChoiceField(choices=Flight.NUM_TICKET_LIST)
    source_location = forms.TypedChoiceField(choices=Flight.AIRPORT_LIST)
    dest_location = forms.TypedChoiceField(choices=Flight.AIRPORT_LIST)
    arrive_date = forms.DateField(initial=datetime.date.today)
    return_date = forms.DateField(initial=datetime.date.today)

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
            raise forms.ValidationError('Invalid input!')

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(validators=[validators.EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

class HotelForm(forms.Form):
    num_rooms = forms.ChoiceField(label="Rooms", choices=Accomodation.NUM_ROOM_LIST)
    num_guests = forms.ChoiceField(label="Guests", choices=Accomodation.NUM_GUEST_LIST)
    location = forms.ChoiceField(label="Location", choices=Accomodation.LOCATION_LIST)
    check_in_date = forms.DateField(label="Check-In Date", initial=datetime.date.today)
    check_out_date = forms.DateField(label="Check-Out Date", initial=datetime.date.today)

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
    num_tickets = forms.ChoiceField(choices=Cruise.NUM_TICKET_LIST)
    source_location = forms.TypedChoiceField(choices=Cruise.SOURCE_LOCATION_LIST)
    dest_location = forms.TypedChoiceField(choices=Cruise.DEST_LOCATION_LIST)
    arrive_date = forms.DateField(initial=datetime.date.today)
    return_date = forms.DateField(initial=datetime.date.today)

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

class RentalForm(forms.Form):
    pass

class PackageForm(forms.Form):
    pass
