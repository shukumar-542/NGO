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
      email = models.EmailField(max_length=250,null=True,blank=True)
      phone = models.CharField(max_length=15, null=False, blank=False)
      about = models.TextField(null=True, blank=True)
      social_links = models.TextField(null=True, blank=True)
      image = models.ImageField(upload_to="volunteer/",
                              default="profile1.png")




class ContactUsMessage(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.EmailField(max_length=250, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

