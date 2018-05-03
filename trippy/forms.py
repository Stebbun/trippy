import datetime
from django import forms
from .models import Flight, Passenger
from django.core import validators

class FlightForm(forms.Form):
    flight_type = forms.ChoiceField(choices=Flight.FLIGHT_TYPE_LIST)
    num_tickets = forms.ChoiceField(choices=Flight.NUM_TICKET_LIST)
    flight_class = forms.ChoiceField(choices=Flight.FLIGHT_CLASS_LIST)
    source_location = forms.TypedChoiceField(choices=Flight.AIRPORT_LIST)
    dest_location = forms.TypedChoiceField(choices=Flight.AIRPORT_LIST)
    arrive_date = forms.DateField(initial=datetime.date.today)

    def clean(self):
        cleaned_data = super(FlightForm, self).clean()
        flight_type = cleaned_data.get('flight_type')
        num_tickets = cleaned_data.get('num_tickets')
        flight_class = cleaned_data.get('flight_class')
        source_location = cleaned_data.get('source_location')
        dest_location = cleaned_data.get('dest_location')
        if not (flight_type or num_tickets or flight_class
                or source_location or dest_location):
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