from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.


class walkrequest(models.Model):
    name            = models.CharField(max_length=100, blank=False)
    phone           = models.IntegerField()
    fromlocation    = models.CharField(max_length=100, blank=False)
    tolocation      = models.CharField(max_length=100, blank=False)
    timerecived     = models.DateTimeField(auto_now_add=True)
    completed       = models.BooleanField(blank=True)


    def __str__(self):
        return self.name
