from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flight/', views.flight, name='flight')
]
