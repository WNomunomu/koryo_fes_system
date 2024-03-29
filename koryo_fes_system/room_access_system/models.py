from django.db import models
from django.utils import timezone

# Create your models here.
class RoomAccessData(models.Model):
    room_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
        
    user_num = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )

    entered_or_left = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )

    entered_or_left_time = models.DateTimeField(
        default=timezone.now,
        blank=False,
        null=False,
    )


class NumberOfPeopleData(models.Model):
    room_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
    )
    
    number_of_people = models.BigIntegerField(
        default=0,
        blank=False,
        null=False,
    )