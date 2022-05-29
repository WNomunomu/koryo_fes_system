from django.apps import AppConfig


class RoomAccessSystemConfig(AppConfig):
    name = 'room_access_system'

    # アプリ起動時にschedule_start()を実行する
    def ready(self):
        print('start!!')
        from .scheduler import schedule_start
        schedule_start()
