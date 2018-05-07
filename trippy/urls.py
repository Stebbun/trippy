from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accomodations/', views.accomodations, name='accomodations'),
    path('flights/', views.flights, name='flights'),
    path('rentals/', views.rentals, name='rentals'),
    path('packages/', views.packages, name='packages'),
    path('payment/', views.payment, name='payment'),
    path('information/', views.information, name='information'),
    path('passenger/', views.passenger, name = 'passenger'),
    path('confirmation/', views.confirmation, name = 'confirmation'),
]
