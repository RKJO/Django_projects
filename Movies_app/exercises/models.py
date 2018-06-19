from django.db import models


# Create your models here.
class Band(models.Model):
    genres = (
        (-1, "not defined"),
        (0, "rock"),
        (1, "metal"),
        (2, "pop"),
        (3, "hip-hop"),
        (4, "electronic"),
        (5, "reggae"),
        (6, "other")
    )
    name = models.CharField(max_length=64)
    year = models.IntegerField(null=True)
    still_active = models.BooleanField(default=True)
    genre = models.IntegerField(choices=genres, default=-1)

    def __str__(self):
        return "{}, {}, {}, active: {}, genre: {}".format(self.id, self.name, self.year, self.still_active, self.genre)


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Article(models.Model):
    statuses = (
        (0, "In progress"),
        (1, "Awaiting approval"),
        (2, "Publishing")
    )
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=statuses, default=0)
    release_start = models.DateField(null=True)
    release_end = models.DateField(null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.title,
                                                    self.author,
                                                    self.content,
                                                    self.date_added,
                                                    self.status,
                                                    self.release_start,
                                                    self.release_end)


class Album(models.Model):
    ratings = tuple(zip(range(0, 6), range(0, 6)))
    title = models.CharField(max_length=128)
    year = models.IntegerField()
    rating = models.IntegerField(choices=ratings)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return "Title: {}, year: {}, rating: {}, band:{}".format(self.title, self.year, self.rating, self.band)


class Song(models.Model):
    title = models.CharField(max_length=128)
    duration = models.TimeField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)