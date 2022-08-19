from django.contrib import admin
from .models import Founder,Voluntieer,ContactUsMessage

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
