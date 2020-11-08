from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import SumCorona, DailyCorona


# Create your views here.

class DailyPageView(generic.ListView):
    template_name = 'cases/daily.html'

    def get_queryset(self):
        return DailyCorona.objects.all()


class SumPageView(generic.ListView):
    template_name = 'cases/sum.html'

    def get_queryset(self):
        return SumCorona.objects.all()
