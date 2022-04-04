from dataclasses import field
from django import forms

from .models import RoomAccessData

class PostForm(forms.ModelForm):
    class Meta:
        model = RoomAccessData
        fields = ('room_name', 'user_num', 'entered_or_left')