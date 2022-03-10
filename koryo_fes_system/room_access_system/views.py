from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import PostForm
from .models import roomAccessData

# Create your views here.
class PostFormView(FormView):
    template_name = 'room_access_system/1-1enter.html'
    form_class = PostForm
    success_url = reverse_lazy('1-1')
    
    def form_valid(self, form):
        room_name = form.cleaned_data['room_name']
        user_num = form.cleaned_data['user_num']
        entered_or_left = form.cleaned_data['entered_or_left']

        roomAccessData.objects.create(
            room_name = room_name,
            user_num = user_num,
            entered_or_left = entered_or_left,
        )

        return super().form_valid(form)