# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import SumCorona, DailyCorona, DailyCasesNew


# Create your views here.

# ListView that shows daily cases by DailyCorona model
class DailyPageView(ListView):
    model = DailyCorona
    template_name = 'cases/deprecated/daily_old.html'
    ordering = '-date'
    paginate_by = 10


# ListView that shows accumulated cases by SumCorona model
class SumPageView(ListView):
    model = SumCorona
    template_name = 'cases/deprecated/sum_old.html'
    ordering = '-date'
    paginate_by = 10


class DailyPageView_2022(ListView):
    model = DailyCasesNew
    template_name = 'cases/new/daily.html'
    ordering = '-date'
    paginated_by = 7


# TemplateView that shows choices page which connects to daily or sum cases
class HomeView(TemplateView):
    template_name = 'home.html'
