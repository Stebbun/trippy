from datetime import datetime, date, timedelta
from django import forms
from .models import Flight, Cruise, Payment
from django.core import validators
from django.contrib.auth.models import User

class FlightForm(forms.Form):
    flight_type = forms.ChoiceField(choices=Flight.FLIGHT_TYPE_LIST)
    num_tickets = forms.ChoiceField(choices=Flight.NUM_TICKET_LIST)
    flight_class = forms.ChoiceField(choices=Flight.FLIGHT_CLASS_LIST)
    source_location = forms.TypedChoiceField(choices=Flight.AIRPORT_LIST)
    dest_location = forms.TypedChoiceField(choices=Flight.AIRPORT_LIST)
    arrive_date = forms.DateField(initial=datetime.now())
    return_date = forms.DateField(initial=datetime.now() + timedelta(days=1))

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

class HotelForm(forms.Form):
    pass

class CruiseForm(forms.Form):
    num_tickets = forms.ChoiceField(choices=Cruise.NUM_TICKET_LIST)
    source_location = forms.TypedChoiceField(choices=Cruise.SOURCE_LOCATION_LIST)
    dest_location = forms.TypedChoiceField(choices=Cruise.DEST_LOCATION_LIST)
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

class RentalForm(forms.Form):
    pass

class PackageForm(forms.Form):
    pass

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
            print("no input")
            raise forms.ValidationError('Invalid input')