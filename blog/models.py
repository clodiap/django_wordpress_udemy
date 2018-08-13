from django.db import models
from django.utils import timezone # to set a publish date to the post

# Create your models here.

# child class of the django model
class Post(models.Model):
  author = models.ForeignKey('auth.User') # reference to a user table
  title = models.CharField(max_length=150, null=True)
  text = models.TextField(null=True)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title
