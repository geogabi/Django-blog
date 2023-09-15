from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Articol(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article', null=True )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=10)
    summary = models.CharField(max_length=50)
    # contents = models.TextField()
    contents = RichTextField(blank=True, null=True)

