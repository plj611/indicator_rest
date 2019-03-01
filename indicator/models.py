from django.db import models

# Create your models here.

#class LighthouseTest(models.Model):
class Lighthouse(models.Model):
   cmd = models.CharField(max_length=2, null=True)
   act = models.CharField(max_length=1, null=True)
   date_time = models.DateTimeField(null=True)
   visit_ip = models.CharField(max_length=15, null=True)

