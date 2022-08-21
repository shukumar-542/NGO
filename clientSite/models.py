from statistics import mode
from django.db import models

# Create your models here.
class Founder(models.Model):
    first_name = models.CharField(max_length=70, null=False, blank=False)
    last_name = models.CharField(max_length=70, null=False, blank=False)
    designation = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="founders/",
                              default="profile1.png")

    def __str__(self):
        return self.first_name


class Voluntieer(models.Model):
    first_name = models.CharField(max_length=70, null=False, blank=False)
    last_name = models.CharField(max_length=70, null=False, blank=False)
    about = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=250,null=True,blank=True)
    facebook = models.URLField(max_length=250, null=True, blank=True)
    linkedin = models.URLField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="volunteer/",
                            default="profile1.png")

    def __str__(self):
        return self.first_name




class ContactUsMessage(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=250, null=True, blank=True)
    message = models.TextField(null=False, blank=False)


    def __str__(self):
        return self.name


class newsAndEvents(models.Model):
    CHOICES = {
        ('news' ,'News'),
        ('event','Event') 
    }
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    type = models.CharField(choices=CHOICES,max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='newsEvent/',null=True, blank=True)


    def __str__(self):
        return self.title

class NewsEventImage(models.Model):
    news_event = models.ForeignKey(to=newsAndEvents,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='newsEvent/')

    def __str__(self):
        return str(self.news_event)


class Project(models.Model):
    CHOICES = {
        ('donor','Donor'),
        ('partner','Partner')
    }

    title = models.CharField(max_length=200, null=False, blank=False)
    donor_partner = models.CharField(max_length=250,null=False, blank=False)
    details = models.TextField(null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=20,choices=CHOICES, null=False, blank=False)
    image = models.ImageField(upload_to="projects/",null=True, blank=True)

    def __str__(self):
        return self.title

class Project_image(models.Model):
    project= models.ForeignKey(to=Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/")

    def __str__(self):
        return str(self.project)

class ImageGallary(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to="gallary/",null=False, blank=False)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    gallery = models.ForeignKey(to=ImageGallary, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="gallery/", null=False, blank=False)

    def __str__(self):
        return str(self.gallery)

class VideoGallery(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    video_link = models.URLField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.title

