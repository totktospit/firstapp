from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sport(models.Model):
      name = models.CharField(max_length=255)
      #users = models.ManyToManyField(PlayField)
       
      def __unicode__(self):
          return self.name
      

class Event(models.Model):
      name = models.CharField(max_length=255)
      description = models.CharField(max_length=3000,null=True)
      time = models.DateTimeField()
      sport = models.ForeignKey(Sport)
      user = models.ForeignKey(User, null=True)

      def __unicode__(self):
          return self.name

class Counter(models.Model):
      number = models.IntegerField(default=0)
