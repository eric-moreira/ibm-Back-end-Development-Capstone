from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


# Create your models here.
'''
concert_name: CharField with a max_length of 255
duration: an IntegerField
city: CharField with a max_length of 255
date: DateField with the default time of now
'''

class Concert(models.Model):
    # concert_name
    concert_name = models.CharField(max_length=255)
    # duration
    duration = models.IntegerField()
    # city
    city = models.CharField(max_length=255)
    # date
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.concert_name


class ConcertAttending(models.Model):
    class AttendingChoices(models.TextChoices):
        NOTHING = "-", _("-")
        NOT_ATTENDING = "Not Attending", _("Not Attending")
        ATTENDING = "Attending", _("Attending")

    concert = models.ForeignKey(
        Concert, null=True, on_delete=models.CASCADE, related_name="attendee"
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    attending = models.CharField(
        max_length=100,
        choices=AttendingChoices.choices,
        default=AttendingChoices.NOTHING,
    )

    class Meta:
        unique_together = ['concert', 'user']

    def __str__(self):
        return self.attending


'''
id: IntegerField as a primary key
pic_url: CharField with max_length of 1000
event_country: CharField with max_length of 255
event_state: CharField with max_length of 255
event_city: CharField with max_length of 255
event_date: DateField with the default time of now
'''

class Photo(models.Model):
    # id
    id = models.IntegerField(_(""), primary_key=True)
    # pic_url
    pic_url = models.CharField(_(""), max_length=1000)
    # event_country
    event_country = models.CharField(_(""), max_length=255)
    # event_state
    event_state = models.CharField(_(""), max_length=255)
    # event_city\
    event_city = models.CharField(_(""), max_length=255)
    # event_date
    event_date = models.DateField(default=timezone.now)

    class Meta:
        managed = False

    def __str__(self):
        return self.pic_url


'''
id: IntegerField as a primary key
title: CharField with max_length of 255
lyrics: TextField
'''

class Song(models.Model):
    # id
    id = models.IntegerField(primary_key=True)
    # title
    title = models.CharField(_(""), max_length=255)
    # lyrics
    lyrics = models.TextField(_(""))

    class Meta:
        managed = False

    def __str__(self):
        return self.title
