from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.NumberOfPeopleApiView.as_view(), name='api'),
]
