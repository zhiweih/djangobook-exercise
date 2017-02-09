from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("<h1>Hello world!</h1>")

def time(request):
    return HttpResponse("<p>It's now %s.</p>" % datetime.datetime.now())

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse("In %s hour(s) it'll be %s." % (offset, dt))
