from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("<h1>Hello world!</h1>")

def time(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_datetime': now})

def date(request):
    now = datetime.datetime.now()
    return render(request, 'current_date.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse("In %s hour(s) it'll be %s." % (offset, dt))

def display_meta(request):
    keys = sorted(request.META.keys())
    html = []
    for key in keys:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (key, request.META[key]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
