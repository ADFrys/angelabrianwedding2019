from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def event(request):
	events = Event.objects
	return render(request, 'event.html', {'events':events})

