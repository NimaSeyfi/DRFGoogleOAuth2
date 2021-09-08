from django.db import models

class AccessKey(models.Model):
    access_token = models.CharField(max_length=250,blank=True,null=True)
    expires_in = models.IntegerField(blank=True,null=True)
    token_type = models.CharField(max_length=30,blank=True,null=True)
    scope = models.CharField(max_length=500,blank=True,null=True)
    id_token = models.CharField(max_length=2000,blank=True,null=True)


class BlockedAccessKey(models.Model):
    ip = models.CharField(max_length=50,blank=True,null=True)
    access_token = models.CharField(max_length=250,blank=True,null=True)
    expires_in = models.IntegerField(blank=True,null=True)
    token_type = models.CharField(max_length=30,blank=True,null=True)
    scope = models.CharField(max_length=500,blank=True,null=True)
    id_token = models.CharField(max_length=2000,blank=True,null=True)