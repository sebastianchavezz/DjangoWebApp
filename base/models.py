from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    #auto_now takes a snapshot everytime 
    updated = models.DateTimeField(auto_now=True) 
    #auto_now_add takes a snapshot everytime we save or create 
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-updated', 'created']


    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #if parent gone, this also gone
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    #auto_now_add takes a snapshot everytime we save or create 
    created = models.DateTimeField(auto_now_add= True)
    
    class Meta:
        ordering = ['-updated', 'created']

    def __str__(self):
        return self.body[:50]

   