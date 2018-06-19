from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return "{} {} {}".format(self.id, self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, related_name="diresctor", on_delete=models.CASCADE)
    screenplay = models.ForeignKey(Person, related_name="sreeenplay", on_delete=models.CASCADE)
    starring = models.ManyToManyField(Person, through='PersonMovie')
    year = models.IntegerField()
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0) ])
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return "{} {} {}".format(self.id, self.title, self.year, self.rating)


class PersonMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=128, null=True)


# Steven = Person.objects.create(first_name="Steven", last_name="Spielberg")
# Martin = Person.objects.create(first_name="Martin", last_name="Scorsese")
# Christopher = Person.objects.create(first_name="Christopher", last_name="Nolan")
# Steven_Sod = Person.objects.create(first_name="Steven", last_name="Soderbergh")
# Ridley = Person.objects.create(first_name="Ridley", last_name="Scott")
# Peter = Person.objects.create(first_name="Peter", last_name="Jackson")


# # 1. Steven Spielberg (E.T., Lista Schindlera)
# # 2. Peter Jackson (Władca Pierścieni, King Kong)
# # 3. Martin Scorsese (Ulice nędzy, Taksówkarz, Wściekły byk, Chłopcy z ferajny)
# # 4. Christopher Nolan (Memento, Mroczny Rycerz)
# # 5. Steven Soderbergh (Co z oczu, to z serca, Traffic)
# # 6. Ridley Scott (Obcy – 8 pasażer Nostromo, Łowca androidów, Gladiator)

# ET = Movie.objects.create(title="E.T.", year=1982, rating=8.9, director=Steven, screenplay=Steven)
# Lista_Schindlera = Movie.objects.create(title="Lista Schindlera", year=1994, rating=7.3, director=Steven, screenplay=Steven)
# Wladca_Pierscieni = Movie.objects.create(title="Władca Pierścieni", year=2002, rating=2005,director=Peter, screenplay=Peter)
# King_Kong = Movie.objects.create(title="King Kong", year=2005, rating=6.6, director=Peter, screenplay=Peter)
# Ulice_nedzy = Movie.objects.create(title="Taksówkarz", year=1973, rating=6.9, director=Martin, screenplay=Martin)
# Taksowkarz = Movie.objects.create(title="Ulice nędzy", year=1976, rating=8.1, director=Martin, screenplay=Martin)
# Wsciekly_byk = Movie.objects.create(title="Wściekły byk", year=1980, rating=8.1, director=Martin, screenplay=Martin)
# Chlopcy_z_ferajny = Movie.objects.create(title="Chłopcy z ferajny", year=1990, rating=8.1, director=Martin, screenplay=Martin)
# Memento = Movie.objects.create(title="Memento", year=2000, rating=8.0, director=Christopher, screenplay=Christopher)
# Mroczny_Rycerz = Movie.objects.create(title="Mroczny Rycerz", year=2008, rating=8.2, director=Christopher, screenplay=Christopher)
# Co_z_oczu = Movie.objects.create(title="Co z oczu, to z serca", year=1998, rating=6.5, director=Steven_Sod, screenplay=Steven_Sod)
# Traffic = Movie.objects.create(title="Traffic", year=2000, rating=7.3, director=Steven_Sod, screenplay=Steven_Sod)
# Obcy = Movie.objects.create(title="Obcy – 8 pasażer Nostromo", year=1980, rating=8.4, director=Ridley, screenplay=Ridley)
# Lowca_androidow = Movie.objects.create(title="Łowca androidów", year=1982, rating=8.1, director=Ridley, screenplay=Ridley)
# Gladiator = Movie.objects.create(title="Gladiator", year=2000, rating=7.1, director=Ridley, screenplay=Ridley)