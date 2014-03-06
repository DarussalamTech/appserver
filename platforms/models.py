from django.db import models
# from apps.models import App
# Create your models here.

class Platform(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class AppPlatform(models.Model):
    app_id=models.ForeignKey('apps.App')
    plat_id=models.ForeignKey(Platform)

    

class Push(models.Model):
    app_platform_id=models.ForeignKey(AppPlatform)
    notification=models.TextField()
    send_date=models.DateTimeField('date published')

class GoogleAnalytics(models.Model):
    app_platform_id=models.ForeignKey(AppPlatform)
    tracking_id=models.CharField(max_length=200)
class Flurry(models.Model):
    app_platform_id=models.ForeignKey(AppPlatform)
    store_id=models.CharField(max_length=400)
    apikey=models.CharField(max_length=200)
    
# class UrbanAirship(models.Model):
#     app_platform_id=models.ForeignKey(AppPlatform)
#     app_UrbanAirship_key=models.CharField(max_length=200) 
    
class Parse(models.Model):
    app_platform_id=models.ForeignKey(AppPlatform)
    application_id=models.CharField(max_length=200) 
    client_key =models.CharField(max_length=200) 
class Facebook(models.Model):
    app_platform_id=models.ForeignKey(AppPlatform)
    app_id=models.CharField(max_length=200)
    app_secret=models.CharField(max_length=300)
    
class Twitter(models.Model):
    app_platform_id=models.ForeignKey(AppPlatform)
    app_id=models.CharField(max_length=200)
    app_secret=models.CharField(max_length=300)
class GooglePlus(models.Model):
    app_platform_id=models.ForeignKey(AppPlatform)
    app_id=models.CharField(max_length=200)
    app_secret=models.CharField(max_length=300)
#     app_Parse=models.ForeignKey(AppPlatform)
class Plugin(models.Model):
    name=models.CharField(max_length=200,blank=True)
#     app_platform_id=models.ForeignKey(AppPlatform)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

#     app_plugin=models.ForeignKey(AppPlatform)
 
# class AppParse(models.Model):
#     parse=models.ForeignKey(Parse)
#     app_platform=models.ForeignKey(AppPlatform)
#     
# class AppFlurry(models.Model):
#     flurry=models.ForeignKey(Flurry)
#     app_platform=models.ForeignKey(AppPlatform)