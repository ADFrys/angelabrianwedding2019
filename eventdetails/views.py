from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Event
from django.shortcuts import render
from .forms import eventForm

def event(request):

	if request.method =="POST":
		form = eventForm(request.POST or None)

		if form.is_valid():
			form.save()
			events = Event.objects
			return render(request, 'event.html', {'events':events})

	else:
		events = Event.objects
		return render(request, 'event.html', {'events':events})




