from django.conf.urls import url
from django.urls import path

from . import views


app_name="account"
urlpatterns = [
    path("", views.TopPageView.as_view(), name="top"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]