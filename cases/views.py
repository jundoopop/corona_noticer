# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from .models import SumCorona, DailyCorona


# Create your views here.

class DailyPageView(ListView):
    template_name = 'cases/daily.html'
    ordering = '-created_at'
    paginate_by = 10

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_at')
        return ordering


class SumPageView(ListView):
    template_name = 'cases/sum.html'
    ordering = 'created_at'
    paginate_by = 10

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_at')
        return ordering
