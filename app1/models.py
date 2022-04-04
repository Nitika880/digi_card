from django.db import models

# Create your models here.
import uuid

import qrcode
from django.contrib.auth.models import AbstractUser
from django.db import models
import random

from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

# Create your models here.


class User(AbstractUser):
    mobile_number = models.CharField(max_length=255)
    user_key = models.UUIDField(default=uuid.uuid4)


class PersonalUserCard(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    full_name = models.CharField(max_length=255)
    Designation_or_profession = models.CharField(max_length=255)
    city_or_state = models.CharField(max_length=255)
    workplace_address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    business_location_link = models.URLField(max_length=255)
    About_us = models.TextField()
    ContactEmail = models.EmailField(max_length=255)
    country = models.CharField(max_length=255)
    country_code = models.IntegerField()
    mobile_number = models.IntegerField()
    business_title = models.CharField(max_length=255)
    business_link = models.URLField(max_length=255)
    services = models.TextField()
    facebook_link = models.URLField(max_length=255, null=True, blank=True)
    twitter_link = models.URLField(max_length=255, null=True, blank=True)
    Instagram_link = models.URLField(max_length=255, null=True, blank=True)
    Linkedin_link = models.URLField(max_length=255, null=True, blank=True)
    Youtube_channel_link = models.URLField(max_length=255, null=True, blank=True)

    profile_img = models.ImageField(upload_to='images/')
    # multi_images = models.FileField()


class Qrcode(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    url = models.URLField(null=True)
    image = models.ImageField(upload_to='qrcode')

    def save(self, *args, **kwargs):
       qrcode_img = qrcode.make(self.url)
       canvas = Image.new("RGB", (300, 300), "white")
       draw = ImageDraw.Draw(canvas)
       canvas.paste(qrcode_img)
       buffer = BytesIO()
       canvas.save(buffer, "PNG")
       self.image.save(f'image{random.randint(0, 9999)}', File(buffer), save=False)
       canvas.close()
       super().save(*args, **kwargs)


