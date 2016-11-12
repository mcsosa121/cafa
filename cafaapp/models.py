from __future__ import unicode_literals

from django.db import models

# Create your models here.
class MikeSosa(models.Model):
	ifyoubelieve = models.CharField(max_length=200)	

# Actual models

class Contract(models.Model):
    cid = models.AutoField(primary_key=True)

class House(models.Model):
    hid = models.AutoField(primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()
    img_raw = models.CharField(max_length=99999999999)
    street = models.CharField(max_length = 100000)
    city = models.CharField(max_length = 100000)
    state = models.CharField(max_length = 100000)
    zip = models.CharField(max_length = 100000)
    contract_ref = models.ForeignKey(Contract)

class Job(models.Model):
    jid = models.AutoField(primary_key=True)
    type = models.CharField(max_length = 10000)
    approval_status = models.BooleanField(default=False)
    comment = models.CharField(max_length = 100000)
    scheduled_time = models.DateField()
    completion_time = models.DateField(blank=True)
    house_ref = models.ForeignKey(House)

class Image(models.Model):
    name = models.CharField(max_length = 100000)
    comment = models.CharField(max_length = 100000)
    raw = models.CharField(max_length=99999999999)
    job_ref = models.ForeignKey(Job)