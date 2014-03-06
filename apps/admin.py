from django.contrib import admin
from apps.models import App,Clients,DeviceType,Category
from apps import forms
from apps.forms import AppForm1,AppForm2,AppForm3,AppForm
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect,Http404
from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.core.context_processors import request
from django.core import serializers
from django.core.urlresolvers import reverse
import json 
from django.views.defaults import shortcut
from django import shortcuts
from django.shortcuts import render_to_response
import cgi
import cgitb
import sys
# Register your models here.
class AppAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name','description','category','playstore_url','itunes_url','platforms','devices','plugins']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
#     inlines = [ChoiceInline]
#     list_filter = ['pub_date']
#     search_fields = ['question']
    def get_urls(self):
            urls = super(AppAdmin, self).get_urls()
            my_urls = patterns('',
                               url(r'^appajaxstep3/$', self.admin_site.admin_view(self.appajaxstep3), name="appajaxstep3"),
                               url(r'^appajaxstep2/$', self.admin_site.admin_view(self.appajaxstep2), name="appajaxstep2"),
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
 
    def appajaxstep3(self,request):
  
        appform3=AppForm3()
        
        if request.is_ajax():
#             form1=
            form=AppForm(request.POST)
            if form.is_valid():
                
                if  form.save() :
                    return HttpResponseRedirect(reverse("admin:index"))
                else:
                    return render_to_response("admin/partials/wizardform3.html",{'appform3':appform3 })
            return render_to_response("admin/partials/wizardform3.html",{'appform3':appform3})    
        
    def appajaxstep2(self,request):
      
        appform2=AppForm2()
        if request.is_ajax():
            
            appform2=AppForm2(request.POST)
            if appform2.is_valid():
#                 if appform2.save():
                    return render_to_response("admin/partials/wizardform2.html",{'appform2':appform2}) 
            else:    
                    return render_to_response("admin/partials/wizardform2.html",{'appform2':appform2})  
    def appajax(self,request):
        print request.POST
        appform1=AppForm1()
        if request.is_ajax():
            
            appform1=AppForm1(request.POST)
            if appform1.is_valid():
                return render_to_response("admin/partials/form.html",{'appform1':appform1} )
   
#                 appform1.empty_permitted
#                 if appform1.save():
#                     return render_to_response("admin/page.html") 
            else: 
                return render_to_response("admin/partials/form.html",{'appform1':appform1} )
   
        #return HttpResponse("")       
        #return HttpResponse("")     
#                 return HttpResponse(appform1 )
#                 return HttpResponse(appform1.errors)
            
#                 return HttpResponse(appform1.errors)
#             print simplejson.dumps(form)
#             data =serializers.deserialize("json", form, ignorenonexistent=True)
           
#              serializers.serialize("xml", form)
#             print form
    
        
#         if request.is_ajax():
#             print 'hello'
#             return True
#         return False
        
class ClientAdmin(admin.ModelAdmin):
        pass
class DeviceTypeAdmin(admin.ModelAdmin):
        pass
class CategoryAdmin(admin.ModelAdmin):
        pass
    




admin.site.register(Category, CategoryAdmin)
admin.site.register(Clients, ClientAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(DeviceType,DeviceTypeAdmin)

