from django.urls import path
from . import views

urlpatterns = [
    path("1-1", views.PostFormView.as_view(), name="1-1")
]
