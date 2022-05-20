from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  id_user = models.IntegerField()
  bio = models.TextField(blank=True)
  profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-image.jpeg')
  location = models.CharField(max_length=100, blank=True)
  firstname = models.CharField(max_length=20, blank=True)
  lastname = models.CharField(max_length=20, blank=True)

  def __str__(self):
      return self.user.username

class Post(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4 )
  user =
  image = 
  caption = 
  created_at =
  no_of_likes =

  