from dataclasses import field
from django import forms

from .models import roomAccessData

class PostForm(forms.ModelForm):
    class Meta:
        model = roomAccessData
        fields = ('room_name', 'user_num', 'entered_or_left')