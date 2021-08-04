from django.db import models
from django.db.models.deletion import CASCADE
from django.forms import widgets
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime
from datetime import date
from ckeditor.fields import RichTextField
# Create your models here.


class User_Image(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='user images')


class Register(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=False)
    date_of_birth = models.DateField(
        null=False, blank=False, )
    account_created_date = models.DateTimeField(default=datetime.now)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    user_photo = models.OneToOneField(
        User_Image, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user_name)
        super(Register, self).save(*args, **kwargs)


class Articles(models.Model):
    writer = models.ForeignKey(Register, on_delete=models.SET_NULL, null=True)
    title = models.CharField(
        max_length=200, blank=False, null=False, unique=True)
    slug = models.SlugField(max_length=200, null=False)
    cover_photo = models.ImageField(
        null=False, blank=False, upload_to='articles/cover_photo')
    blog_created_date = models.DateField(default=date.today)
    tag=models.CharField(max_length=50, blank=False, null=False)
    content = RichTextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Articles, self).save(*args, **kwargs)
