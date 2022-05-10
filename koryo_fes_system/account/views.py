from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from . import forms


class TopPageView(TemplateView):
    template_name = "account/top.html"

# ログインページ
class LiginView(LoginView):
    form_class = forms.LoginForm
    template_name = "account/login.html"

# ログアウトページ
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "account/login.html"