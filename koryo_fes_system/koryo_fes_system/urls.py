"""koryo_fes_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# from django.contrib.auth.models import Group


admin.site.site_title = '蛟龍祭入場管理システム Marronnier'
admin.site.site_header = '蛟龍祭入場管理システム Marronnier'
admin.site.index_title = 'メニュー'
# admin.site.unregister(Group)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('room_access_system.urls')),
    path('api/', include("number_of_people_api.urls")),
    # path('', RedirectView.as_view(url='/home/')),
    path('', include('account.urls')),
]