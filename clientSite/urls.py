from turtle import home
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('about/', views.about.as_view(), name='about'),
    path('donar-partnership', views.donorPartnership.as_view(),name='donor-parntership')
    

]