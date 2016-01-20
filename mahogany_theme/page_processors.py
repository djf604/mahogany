__author__ = 'Dominic Fitzgerald'
from mezzanine.pages.page_processors import processor_for

from models import HomePage, Event

@processor_for(HomePage)
def home(request, page):
    events = Event.objects.all()
    return {'events': events}