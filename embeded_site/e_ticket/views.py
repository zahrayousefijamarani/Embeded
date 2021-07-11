import os
from pathlib import Path
import requests

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from barcode import Code39
from django.shortcuts import render
from django.urls import reverse
from barcode.writer import ImageWriter

from e_ticket.models import Film, SANS, Ticket, BoughtTicket

from embeded_site.settings import BASE_DIR
from embeded_site.settings import BASE_DIR


def index(request):
    films = Film.objects.all()
    sans = SANS
    return render(request, './e_ticket/index.html', context={'films': films, 'sans': sans, })


def submit(request):
    try:
        sans = request.POST['sans']
        name = request.POST['name']
        film = request.POST['film']

        f = Ticket(name=name, sans=sans)
        f.save()
        f.film.add(Film.objects.get(name=film))

        # Make sure to pass the number as string
        number = str(f.id)
        if len(number) < 13:
            number += 'A'
            for i in range(0, 13 - len(number)):
                if i > 9:
                    number += str(i - 1)
                number += str(i)
        print(number)

        my_code = Code39(number)
        b = BoughtTicket(code=my_code.get_fullcode(), ticket_id=f.id)
        b.save()
        # Our barcode is ready. Let's save it.
        my_code.save(os.path.join(BASE_DIR, 'e_ticket/static/e_ticket/images/', str(f.id)))
        return render(request, './e_ticket/show.html',
                      context={'image': '../../static/e_ticket/images/' + str(f.id) + ".svg"})

    except:
        raise Http404("something is wrong !")


people = 0


def get_barcode(request, barcode):
    global people
    b = BoughtTicket.objects.get(code=barcode)
    if b:
        people += 1
        r = requests.get('http://192.168.1.10/plus/')
        print("-----------------------------------------")
        print(r.status_code )
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)
