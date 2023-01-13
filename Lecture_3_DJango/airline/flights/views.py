from django.shortcuts import render
from django.http import HttpResponse
from .models import Flights
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flightlist":Flights.objects.all()
    })

def flight(request, flight_id) :
    flightInfo  =  Flights.objects.get(id=flight_id)
    # or  flightInfo  =  Flights.objects.get(pk=flight_id)
   
    return render(request, "flights/flight.html", {
        "flight":flightInfo
    })
    # return HttpResponse(flightInfo.origin)