from django.db import models
from django.contrib.auth.models import User

import os
from django.urls import reverse





class User(models.Model):
    email = models.EmailField(unique=True)
    # username = models.CharField(max_length=150, unique=True)


    def __str__(self):
        return self.email
    

class UserProfileInfo(models.Model):
    username = models.CharField(max_length=150, null=True, unique=True)
    Customer_location = models.CharField(max_length=150, null=True, unique=True, blank=False)
    phone_number = models.CharField(max_length=11, blank=True) 

    def __str__(self):
        return self.username
    
    
# Create your models here.
class Food(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200,  null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    body3 = models.TextField(max_length=500, null=True, blank=True)
    body4 = models.TextField(max_length=500, null=True, blank=True)
    body5 = models.TextField(max_length=500, null=True, blank=True)
    body6 = models.TextField(max_length=500, null=True, blank=True)
    body7 = models.TextField(max_length=500, null=True, blank=True)
    body8 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    Commenter = models.CharField(max_length= 50)
    body = models.TextField()
    post = models.ForeignKey(Food, on_delete= models.CASCADE, related_name= 'comments')
    def __str__(self):
        return self.body
    
    
def path_and_rename(instance, filename):
    upload_to = 'images_uploaded'
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


 

class AboutUs(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200)
    body = models.TextField(max_length=500)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    


class Location(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    body3 = models.TextField(max_length=500, null=True, blank=True)
    body4 = models.TextField(max_length=500, null=True, blank=True)
    

    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
    

class EPLANNING(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True )
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title


class EWEDDING(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    
class EBIRTHDAY(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body

class ENAMING(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body

class EANNIVERSARY(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body

class EDIETING(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body

class EHOTEL(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body

class ECAFETERIA(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body

class ERENDERING(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body


class RiteGallery(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.body
