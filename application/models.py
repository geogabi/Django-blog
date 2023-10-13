import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model as user_model
from django.utils.timezone import localtime, now
User = user_model()

class Article(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article', null=True )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=200)
    contents = RichTextField(blank=True, null=True)
    created = models.DateTimeField(default=localtime(), blank=True)
