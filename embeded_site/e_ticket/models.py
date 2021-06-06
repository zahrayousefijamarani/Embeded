from django.db import models
from django.forms import ModelForm, forms

SANS = ["Morning", "Evening", "Night"]


class Film(models.Model):
    name = models.CharField(max_length=100)


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    sans = models.CharField(max_length=7)
    film = models.ManyToManyField(Film)

    def __str__(self):
        return self.name


class BoughtTicket(models.Model):
    code = models.CharField(max_length=100)
    ticket_id = models.IntegerField()

    def __str__(self):
        return self.code
