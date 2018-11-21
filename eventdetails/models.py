from django.db import models

class Event(models.Model):
	summary = models.CharField(max_length=200)

