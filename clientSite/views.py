from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class home(TemplateView):
      template_name = 'clientSite/home.html'

class about(TemplateView):
      template_name='clientSite/about.html'

class donorPartnership(TemplateView):
      template_name ='clientSite/donor-partner.html'