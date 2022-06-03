from django.urls import include, path

from . import views

urlpatterns = [
    path('copy_check/<slug:user_num>', views.CopyCheckDataApi.as_view(), name='api'),
]
