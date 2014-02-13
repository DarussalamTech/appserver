from django.db import models
# from apps.models import App
# Create your models here.
class Platform(models.Model):
    name=models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
class Plugin(models.Model):
    name=models.CharField(max_length=200)
        


class Push(models.Model):
   
    notification=models.TextField()
    send_date=models.DateTimeField('date published')

class GoogleAnalytics(models.Model):
    tracking_id=models.CharField(max_length=200)
class Flurry(models.Model):
    store_id=models.CharField(max_length=400)
    apikey=models.CharField(max_length=200)
    
class UrbanAirship(models.Model):
    app_UrbanAirship_key=models.CharField(max_length=200) 
    
class Parse(models.Model):
    application_id=models.CharField(max_length=200) 
    client_key =models.CharField(max_length=200) 
class Facebook(models.Model):
    app_id=models.CharField(max_length=200)
    app_secret=models.CharField(max_length=300)
    
class Twitter(models.Model):
    app_id=models.CharField(max_length=200)
    app_secret=models.CharField(max_length=300)
#     app_Parse=models.ForeignKey(AppPlatform)

class AppPlatform(models.Model):
    app_id=models.ForeignKey('apps.App')
    plat_id=models.ForeignKey(Platform)
    plugin=models.ForeignKey(Plugin)
    push=models.ForeignKey(Push)
    facebook=models.ForeignKey(Facebook)
    parse=models.ForeignKey(Parse)
    twitter=models.ForeignKey(Twitter)
    google_analytics=models.ForeignKey(GoogleAnalytics)
    urban_airship=models.ForeignKey(UrbanAirship)
    
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
#     app_plugin=models.ForeignKey(AppPlatform)
 
class AppParse(models.Model):
    parse=models.ForeignKey(Parse)
    app_platform=models.ForeignKey(AppPlatform)
    
class AppFlurry(models.Model):
    flurry=models.ForeignKey(Flurry)
    app_platform=models.ForeignKey(AppPlatform)