from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=45)
  content = models.TextField()
  date = models.DateTimeField()
  published = models.IntegerField(default=0)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


class Unregistered_user(models.Model):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.EmailField(max_length=40, unique=True)
  comments = models.CharField(max_length=1000)


class Event_subscriptions(models.Model):
  id = models.AutoField(primary_key=True)
  event_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
  unregistered_user_id = models.ForeignKey(Unregistered_user, on_delete=models.CASCADE) 