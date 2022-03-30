from django.contrib import admin
from .models import roomAccessData

# Register your models here.
@admin.register(roomAccessData)
class RoomAccessDataAdmin(admin.ModelAdmin):
    model = roomAccessData
    list_display = ["room_name", "user_num", "entered_or_left", "entered_or_left_time"]