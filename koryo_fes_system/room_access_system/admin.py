from django.contrib import admin
from .models import RoomAccessData

# Register your models here.
@admin.register(RoomAccessData)
class RoomAccessDataAdmin(admin.ModelAdmin):
    model = RoomAccessData
    list_display = ["room_name", "user_num", "entered_or_left", "entered_or_left_time"]