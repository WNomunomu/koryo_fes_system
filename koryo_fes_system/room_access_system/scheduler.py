from django.conf import settings

from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from .models import RoomAccessData, NumberOfPeopleData
from django.db.models import Sum


# 各部屋の人数をデータベースから計算して、もう一つのデータベースに保存する関数
def calculate_number_of_people():
    room_access_data = RoomAccessData.objects
    number_of_people_data = NumberOfPeopleData.objects

    number_of_people_data.all().delete() # このデータベースは毎回上書きする必要があるので、一度データを全て消去する

    saved_room_name_list = room_access_data.values_list('room_name', flat=True) # データベースからroom_nameのカラムのデータを全部取得
    room_name_list = list(set(saved_room_name_list)) # 上で取得したリストの重複を削除
    
    for room_name in room_name_list:
        room_data = room_access_data.filter(room_name=room_name).all()
        number_of_people = room_data.aggregate(Sum('entered_or_left')).get('entered_or_left__sum')

        data = NumberOfPeopleData(room_name=room_name, number_of_people=number_of_people)
        data.save()

    print('データが保存されました。')


# 300秒おきに上の関数を実行
def schedule_start():
    scheduler = BackgroundScheduler()
   
    scheduler.add_job(calculate_number_of_people, 'interval', seconds=300) # schedule
    scheduler.start()