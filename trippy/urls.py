from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels/', views.hotels, name='hotels'),
    path('flights/', views.flights, name='flights'),
    path('cruises/', views.cruises, name='cruises'),
    path('rentals/', views.rentals, name='rentals'),
    path('packages/', views.packages, name='packages'),
    path('payment/', views.payment, name='payment'),
    path('information/', views.information, name='information'),
]
