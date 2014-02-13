from django.contrib import admin
from apps.models import App,Clients,DeviceType
from apps import forms
from apps.forms import AppForm1,AppForm2,AppForm3
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.core.context_processors import request
from django.core import serializers

# Register your models here.
class AppAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','icon','description','category','android','ios','tab','ipad','iphone','android_phone','playstore_url','itunes_url','platforms']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
#     inlines = [ChoiceInline]
#     list_filter = ['pub_date']
#     search_fields = ['question']
    def get_urls(self):
            urls = super(AppAdmin, self).get_urls()
            my_urls = patterns('',
                               url(r'^appajax/$', self.admin_site.admin_view(self.appajax), name="appajax"),
                               url(r'^appwizard/$', self.admin_site.admin_view(self.create_app_wizard), name="appwizard")
                               )
            my_urls = my_urls + urls
            return my_urls
    def create_app_wizard(self, request,extra_context=None):
        appform1=AppForm1
        appform2=AppForm2
        appform3=AppForm3
        return render(request,'admin/wizard.html',{'appform1':appform1,'appform2':appform2,'appform3':appform3})
    
    def appajax(self,request):
        
        if request.is_ajax():
            form=AppForm1(request.POST)
            form.is_valid()
            print form.errors
#             data =serializers.deserialize("json", form, ignorenonexistent=True)
           
#              serializers.serialize("xml", form)
#             print form
        return HttpResponse(form.errors)
#         if request.is_ajax():
#             print 'hello'
#             return True
#         return False
        
class ClientAdmin(admin.ModelAdmin):
        pass
class DeviceTypeAdmin(admin.ModelAdmin):
        pass
    




admin.site.register(Clients, ClientAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(DeviceType,DeviceTypeAdmin)

