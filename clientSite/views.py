from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Founder,Voluntieer,newsAndEvents,Project

# Create your views here.
class home(TemplateView):
      template_name = 'clientSite/home.html'

class about(ListView):
      model = Founder
      template_name='clientSite/about.html'

      def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            
            context["founder_list"] = Founder.objects.all()[0:3]
            context["voluntieer_list"] =Voluntieer.objects.all()[0:4]
            # print(context)
            return context


class donorPartnership(TemplateView):
      model =Project
      template_name ='clientSite/donor-partner.html'
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['donor_project'] = Project.objects.filter(category='donor')[0:10]
            context['pratner_project'] = Project.objects.filter(category='partner')[0:10]
            return context
      
class contact(TemplateView):
      template_name ='clientSite/contact.html'

class Projects(TemplateView):
      template_name ='clientSite/projects.html'
      def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context

class Projects_details(TemplateView):
      template_name ='clientSite/projects-details.html'

class news(ListView):
      model = newsAndEvents
      ordering=['date']
      paginate_by= 2
      template_name ='clientSite/news.html'
      
class image_gallary(TemplateView):
      template_name ='clientSite/image-gallary.html'

class video_gallary(TemplateView):
      template_name ='clientSite/video-gallery.html'

