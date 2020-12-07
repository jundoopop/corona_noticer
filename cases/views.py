# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import SumCorona, DailyCorona


# Create your views here.

class DailyPageView(ListView):
    model = DailyCorona
    template_name = 'cases/daily.html'
    ordering = '-date'
    paginate_by = 10


class SumPageView(ListView):
    model = SumCorona
    template_name = 'cases/sum.html'
    ordering = '-date'
    paginate_by = 10


class HomeView(TemplateView):
    template_name = 'home.html'
