from django.db import models
from django.template.defaultfilters import default
from platforms.models import Platform,Plugin
from django.core.validators import URLValidator
class Category(models.Model):
    cat_name=models.CharField(max_length=100)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.cat_name
class Clients(models.Model):
    email=models.EmailField(blank=True)
    device_id=models.IntegerField(default=0)
    
class DeviceType(models.Model):
    name=models.CharField(max_length=300)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
# class device(models.m):


class AppPlatforms(models.Model):
    app_id=models.ForeignKey('apps.App')
    plat_id=models.ForeignKey('platforms.Platform')
    
    class Meta:
        db_table = 'apps_app_platforms'
    
class App(models.Model):
    name=models.CharField(max_length=100,unique=True)
    icon=models.FileField(upload_to="media/%Y/%m/%d" ,null=True)
    pub_date = models.DateTimeField('Created', auto_now=True)
    description=models.TextField()
    category=models.ForeignKey(Category)
    
    playstore_url=models.URLField(validators=[URLValidator()])
    itunes_url=models.URLField(validators=[URLValidator()])
    platforms = models.ManyToManyField(Platform)
    clients = models.ManyToManyField(Clients)
    devices = models.ManyToManyField(DeviceType)
    plugins=models.ManyToManyField(Plugin)
    create_user=models.ForeignKey('auth.User')
    def __unicode__(self):  # Python 3: def __str__(self):
        return u"%s %s %s %s %s %s %s %s %s %s" % (self.name, self.icon,self.pub_date,self.description,self.category
                           ,self.playstore_url,self.itunes_url,self.platforms,self.clients,self.plugins)
    
#         model = App

class AppPlugin(models.Model):
    app_id=models.ForeignKey(App)  
    plugin_id = models.ForeignKey(Plugin)
    
    class Meta:
        db_table = 'apps_app_plugins'
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return u"%s %s" % (self.plugin_id,self.app_id)

class AppClients(models.Model):
    app_id=models.ForeignKey(App)
    client_id=models.ForeignKey(Clients)


class Device(models.Model):
    deviceIdentifier=models.CharField(max_length=300)
    client=models.ManyToManyField(Clients)
    

