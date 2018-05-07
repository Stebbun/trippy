from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Location)
admin.site.register(Accomodation)
admin.site.register(Transportation)
admin.site.register(Flight)
admin.site.register(CarRental)
admin.site.register(Group)
admin.site.register(Passenger)
admin.site.register(Payment)
admin.site.register(Airport)
