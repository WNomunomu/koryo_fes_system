from django.urls import path
from . import views

urlpatterns = [
    path('room_access/<slug:room_name>/<slug:enter_or_leave>', views.PostFormView.as_view(), name="room_access"),
]