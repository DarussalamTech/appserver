from django.db import models
from django.template.defaultfilters import default
from platforms.models import Platform


class Category(models.Model):
    cat_name=models.CharField(max_length=100)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.cat_name
class Clients(models.Model):
    email=models.EmailField()
    device_id=models.IntegerField(default=0)
    
class DeviceType(models.Model):
    name=models.CharField(max_length=300)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
# class device(models.m):
    
class App(models.Model):
    name=models.CharField(max_length=100)
    icon=models.FileField(upload_to='/%Y_%m_%d/')
    pub_date = models.DateTimeField('date published')
    description=models.TextField()
    category=models.ForeignKey(Category)
    playstore_url=models.CharField(max_length=500)
    itunes_url=models.CharField(max_length=500)
    platforms = models.ManyToManyField(Platform)
    clients = models.ManyToManyField(Clients)
    devices = models.ManyToManyField(DeviceType)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return u"%s %s" % (self.name, self.icon,self.description,self.category
                           ,self.playstore_url,self.itunes_url,self.platforms,self.clients)

    
class AppClients(models.Model):
    app_id=models.ForeignKey(App)
    client_id=models.ForeignKey(Clients)


class Device(models.Model):
    deviceIdentifier=models.CharField(max_length=300)
    client=models.ManyToManyField(Clients)
    
