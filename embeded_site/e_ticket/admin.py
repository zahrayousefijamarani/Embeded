from django.contrib import admin

from .models import Film, Ticket, BoughtTicket

admin.site.register(Film)
admin.site.register(Ticket)
admin.site.register(BoughtTicket)
