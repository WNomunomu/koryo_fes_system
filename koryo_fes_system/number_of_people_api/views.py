from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum
import json

from room_access_system.models import RoomAccessData

# Create your views here.
class NumberOfPeopleApiView(View):
    def get(self, request):
        room_access_data = RoomAccessData.objects

        saved_room_name_list = room_access_data.values_list('room_name', flat=True) # データベースからroom_nameのカラムのデータを全部取得
        room_name_list = list(set(saved_room_name_list)) # 上で取得したリストの重複を削除
        
        number_of_people_dict = {}

        for room_name in room_name_list:
            room_data = room_access_data.filter(room_name=room_name).all()
            number_of_people = room_data.aggregate(Sum('entered_or_left')).get('entered_or_left__sum')

            number_of_people_dict.setdefault(room_name, number_of_people)


        json_data = json.dumps(number_of_people_dict)

        return HttpResponse(json_data, content_type="application/json")
