from django.urls import path
from . import views


app_name="room_access_system"
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('room_access/<slug:room_name>/<slug:enter_or_leave>', views.RoomAccessView.as_view(), name="room_access"),
    path('ajax_post', views.ajax_response, name='ajax_post'),
]
