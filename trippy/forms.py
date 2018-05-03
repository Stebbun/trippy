import datetime
from django import forms
from .models import Flight

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
