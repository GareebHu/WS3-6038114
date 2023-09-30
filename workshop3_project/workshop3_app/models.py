# workshop3_app/models.py
from django.db import models

class Movie(models.Model):
    Name = models.TextField()
    Year = models.TextField()
    Genre = models.TextField()

class Attend(models.Model):
    ATTN_Number = models.IntegerField()
    Movie_Name = models.TextField()
    Seat_Number = models.TextField()
    Show_Time = models.TextField()