from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=30)


class Coordinate(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    altitude = models.IntegerField()
    accuracy = models.IntegerField()
    heading = models.IntegerField()
    speed = models.IntegerField()


class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')


class Point(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    coordinate = models.OneToOneField(
        Coordinate,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
