#coding:utf-8
from django.db import models
class monitors(models.Model):
    servername = models.CharField(max_length=30)
    item = models.CharField(max_length=30)
    value = models.CharField(max_length=30,default="")
    serverip = models.GenericIPAddressField()
    time = models.DateTimeField()
    def __unicode__(self):
        return self.servername


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.username

class question(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    body = models.TextField()
    timestamp = models.DateTimeField()

class Experience(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    body = models.TextField()
    timestamp = models.DateTimeField()

class zaj(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    body = models.TextField()
    timestamp = models.DateTimeField()

