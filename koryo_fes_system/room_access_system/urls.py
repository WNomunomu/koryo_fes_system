from django.urls import path
from . import views

urlpatterns = [
    path('enter/<slug:room_name>', views.PostFormView.as_view(), name="enter"),
]