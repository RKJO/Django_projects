from exercises.bands_script import update
from exercises.models import Band
from random import randint, choice
from exercises.models import *

def hello():
    return "Hello Word!"


def no_year():
    bands = Band.objects.filter(year=None)
    for band in bands:
        print(band.id, band.name)
    return bands


def new_year(bands):
    for band in bands:
        band.year = randint(1951, 2018)
        band.save()


def no_genre():
    bands = Band.objects.filter(genre=-1)
    for band in bands:
        band.genre = randint(0, 6)


def update():
    bands = Band.objects.filter()
    for band in bands:
        if band.genre == -1:
            band.genre = randint(0, 6)
        band.still_active = choice([True, False])
        band.save()


def new_year(bands):
    for band in bands:
        band.year = randint(1951, 2018)
        band.save()


bands = Band.objects.all()
