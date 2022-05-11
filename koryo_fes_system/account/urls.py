from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from . import views


app_name="account"
urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]