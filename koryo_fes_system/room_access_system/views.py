from audioop import reverse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import PostForm
from .models import roomAccessData

# Create your views here.
class HomeView(TemplateView):
    template_name = 'room_access_system/home.html'


class PostFormView(FormView):
    def get(self, request, room_name, enter_or_leave):
        if enter_or_leave == 'enter':
            parameter = 1
        elif enter_or_leave == 'leave':
            parameter = -1

        form = PostForm(request.GET or None, initial={'room_name': room_name, 'entered_or_left': parameter})

        return render(request, 'room_access_system/room_access.html', dict(form=form))

    form_class = PostForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('room_access', kwargs={'room_name': self.kwargs['room_name'], 'enter_or_leave': self.kwargs['enter_or_leave']})

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