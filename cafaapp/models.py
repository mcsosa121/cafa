from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MikeSosa(models.Model):
	ifyoubelieve = models.CharField(max_length=200)	

# Actual models

class House(models.Model):
    hid = models.AutoField(primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()
    img_docfile = models.ImageField(upload_to='documents/%Y/%m/%d')
    street = models.CharField(max_length = 100000)
    city = models.CharField(max_length = 100000)
    state = models.CharField(max_length = 100000)
    zip = models.CharField(max_length = 100000)

class Job(models.Model):
    jid = models.AutoField(primary_key=True)
    type = models.CharField(max_length = 10000)
    approval_status = models.BooleanField(default=False)
    request_comment = models.CharField(max_length = 100000, default='request')
    completion_comment = models.CharField(max_length = 100000, default='incomplete')
    scheduled_time = models.DateTimeField() #2016-12-11 12:11
    completion_time = models.DateTimeField(null=True)
    house_ref = models.ForeignKey(House)

class Image(models.Model):
    name = models.CharField(max_length = 100000)
    comment = models.CharField(max_length = 100000)
    docfile = models.ImageField(upload_to='documents/%Y/%m/%d')
    job_ref = models.ForeignKey(Job)