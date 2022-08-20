from django.contrib import admin
from .models import Founder,Voluntieer,ContactUsMessage,newsAndEvents,NewsEventImage,Project,Project_image,ImageGallary,GalleryImage,VideoGallery

# Register your models here.
@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Founder._meta.get_fields()]


@admin.register(Voluntieer)
class VolunteerAdmin(admin.ModelAdmin):
      list_display =[f.name for f in Voluntieer._meta.get_fields()]



@admin.register(ContactUsMessage)
class ContactUsMessageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ContactUsMessage._meta.get_fields()]


@admin.register(newsAndEvents)
class newsAndEventsAdmin(admin.ModelAdmin):
    list_display = ['title','description','date','type']

@admin.register(NewsEventImage)
class NewsEventImageAdmin(admin.ModelAdmin):
    list_display = ['news_event']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','details','start_date','end_date','category']

@admin.register(Project_image)
class Project_imageAdmin(admin.ModelAdmin):
    list_display = ['project']

@admin.register(ImageGallary)
class ImageGallaryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['gallery']

@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ['title']

