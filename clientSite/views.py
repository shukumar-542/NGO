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
            return context

class Projects_details(TemplateView):
      template_name ='clientSite/projects-details.html'

class news(TemplateView):
      template_name ='clientSite/news.html'
      
class image_gallary(TemplateView):
      template_name ='clientSite/image-gallary.html'

class video_gallary(TemplateView):
      template_name ='clientSite/video-gallery.html'

