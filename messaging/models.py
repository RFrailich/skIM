from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
#username, (encrypts) password, email, first_name, last_name, date_joined, last_login
    
class Conversation(models.Model):
    users = models.ManyToManyField(User)
    
class Message(models.Model):
    body = models.CharField(max_length=1000)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sent_date = models.DateField()
