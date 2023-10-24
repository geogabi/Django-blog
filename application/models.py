from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model as user_model
from django.utils.timezone import localtime
User = user_model()

class Article(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article', null=True )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, default='', null=False)
    summary = models.CharField(max_length=200)
    contents = RichTextField(blank=True, null=True)
    blog_picture = models.ImageField(null=True, blank=True, upload_to='images/', default='images/none_picture.jpg')
    created = models.DateTimeField(default=localtime(), blank=True)
