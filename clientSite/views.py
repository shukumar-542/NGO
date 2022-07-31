from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class home(TemplateView):
      template_name = 'clientSite/home.html'

class about(TemplateView):
      template_name='clientSite/about.html'

class donorPartnership(TemplateView):
      template_name ='clientSite/donor-partner.html'
      
class contact(TemplateView):
      template_name ='clientSite/contact.html'

class Projects(TemplateView):
      template_name ='clientSite/projects.html'
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

        # for Dynamic url argument value
            type = kwargs
            myType = context["type"]

            return context

class news(TemplateView):
      template_name ='clientSite/news.html'

