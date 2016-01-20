__author__ = 'Dominic Fitzgerald'
from django.db import models

from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.core.fields import FileField


class HomePage(Page, RichText):
    heading = models.CharField(max_length=256)

class Event(models.Model):
    name = models.CharField(max_length=512)
    time = models.DateTimeField()
    location = models.CharField(max_length=512)
    details = models.TextField()
    image = models.ImageField(null=True, blank=True)

