from django.shortcuts import render

# Create your views here.
# django_web_scraping_example/views.py
from scraping.models import News  # bring News into the views
from django.views import generic


class HomePageView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'articles'

    # assign "News" object list to the object "articles"
    # pass news objects as queryset for listview
    def get_queryset(self):
        return News.objects.all()
