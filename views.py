from django.shortcuts import render
from django.http import Http404, HttpResponse 

from .models import Event, Counter

# Create your views here.

def index(request):
    falota = ""
    for k in request.session.keys():
        falota += str(k) + "\n"
    return HttpResponse("Hello, world. You're at the sports index.\n" + falota)

def seeEvent(request, event_id):
    try:
       event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
       raise Http404("Event does not exist")
    return render(request, 'sports/detail.html',{'event':event})

def createEvent(request):
    return HttpResponse("It will work!")

def seeCounter(request):
    number = Counter.objects.get(pk=1).number
    return HttpResponse(str(number))
