from django.db import models

# Create your models here.
class roomAccessData(models.Model):
    room_name = models.CharField(
        max_length=20,
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
        auto_now=True,
        editable=False,
        blank=False,
        null=False,
    )