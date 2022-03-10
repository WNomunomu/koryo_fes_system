from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import PostForm
from .models import roomAccessData

# Create your views here.
class PostFormView(FormView):
    def get(self, request, room_name):
        form = PostForm(request.GET or None, initial={'room_name': room_name})

        return render(request, 'room_access_system/enter.html', dict(form=form))
    
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