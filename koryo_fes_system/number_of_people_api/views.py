from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models import Sum

from room_access_system.models import RoomAccessData

# Create your views here.
class NumberOfPeopleApiView(View):
    def get(self, request):
        room_name = request.GET['room_name']
        room_access_data = RoomAccessData.objects
        room_data = room_access_data.filter(room_name=room_name).all()
        number_of_people = room_data.aggregate(Sum('entered_or_left'))

        json_data = {
            "room_name": room_name,
            "number_of_people": number_of_people
        }

        return JsonResponse(json_data)
