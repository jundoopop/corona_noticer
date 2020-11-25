from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import SumCorona, DailyCorona


# Create your views here.

class DailyPageView(generic.ListView):
    template_name = 'cases/daily.html'
    ordering = '-created_at'
    paginate_by = 10

    def get_queryset(self):
        return DailyCorona.objects.all()


class SumPageView(generic.ListView):
    template_name = 'cases/sum.html'
    ordering = '-created_at'
    paginate_by = 10

    def get_queryset(self):
        return SumCorona.objects.all()
