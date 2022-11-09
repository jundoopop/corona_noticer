# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import SumCorona, DailyCorona


# Create your views here.

# ListView that shows daily cases by DailyCorona model
class DailyPageView(ListView):
    model = DailyCorona
    template_name = 'cases/daily_old.html'
    ordering = '-date'
    paginate_by = 10


# ListView that shows accumulated cases by SumCorona model
class SumPageView(ListView):
    model = SumCorona
    template_name = 'cases/sum_old.html'
    ordering = '-date'
    paginate_by = 10


# TemplateView that shows choices page which connects to daily or sum cases
class HomeView(TemplateView):
    template_name = 'home.html'
