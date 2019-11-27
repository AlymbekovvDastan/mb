from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
	template_name = 'pages/home_html.html'


class AboutPageView(TemplateView):
	template_name = 'pages/about.html'

