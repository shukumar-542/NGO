from turtle import home
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('about/', views.about.as_view(), name='about'),
    path('donar-partnership', views.donorPartnership.as_view(),name='donor-parntership'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('projects/<str:type>/', views.Projects.as_view(), name='projects'),
    path('projects-details/<int:pk>/', views.Projects_details.as_view(), name='projects-details'),
    path('news/', views.news.as_view(), name='news'),
    path('image-gallary/',views.image_gallary.as_view(), name='image_gallary'),
    path('video-gallary/',views.video_gallary.as_view(), name='video_gallary'),
    

]