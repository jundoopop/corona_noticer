# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView
from .models import SumCorona, DailyCorona


# Create your views here.

class DailyPageView(ListView):
    template_name = 'cases/daily.html'
    ordering = '-created_at'
    paginate_by = 10

    def get_queryset(self):
        return SumCorona.objects.order_by('-created_at')


class SumPageView(ListView):
    template_name = 'cases/sum.html'
    ordering = 'created_at'
    paginate_by = 10

    def get_queryset(self):
        return SumCorona.objects.order_by('-created_at')
