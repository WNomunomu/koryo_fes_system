from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import json

from .forms import PostForm
from .models import RoomAccessData, NumberOfPeopleData

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'room_access_system/home.html'


"""
# このviewは今は使っていないですが、一応残しておきます。by野村
class PostFormView(FormView):
    # 最初にurlでアクセスしたときの処理
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

    # postされたデータの処理
    def form_valid(self, form):
        room_name = form.cleaned_data['room_name']
        user_num = form.cleaned_data['user_num']
        entered_or_left = form.cleaned_data['entered_or_left']

        RoomAccessData.objects.create(
            room_name = room_name,
            user_num = user_num,
            entered_or_left = entered_or_left,
        )

        return super().form_valid(form)
"""


# ajaxの処理
@login_required
def ajax_response(request):
    if request.method == 'POST':

        room_name = request.POST.get('room_name')
        user_num = int(request.POST.get('user_num'))
        entered_or_left = request.POST.get('entered_or_left')


        RoomAccessData.objects.create(
            room_name = room_name,
            user_num = user_num,
            entered_or_left = entered_or_left,
        )
        
                    
        return HttpResponse("こんにちは")


class RoomAccessView(LoginRequiredMixin, View):
    def get(self, request, room_name, enter_or_leave):
        if enter_or_leave == 'enter':
            parameter = 1
        elif enter_or_leave == 'leave':
            parameter = -1

        form = PostForm(request.GET or None, initial={'room_name': room_name, 'entered_or_left': parameter})

        return render(request, 'room_access_system/room_access.html', dict(form=form))


class CongestionLevelView(TemplateView):

    template_name = 'room_access_system/congestion_level.html'

    def get_context_data(self, **kwargs):

        number_of_people_data = NumberOfPeopleData.objects.all()

        context = super().get_context_data(**kwargs)
        context['data'] = number_of_people_data

        return context

    # def get(self, request):

    #     context = {
    #         'data': number_of_people_data,
    #     }

    #     return render(request, 'room_access_system/congestion_level.html', context)