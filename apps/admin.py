from django.contrib import admin
from apps.models import App,Clients,DeviceType,Category
from apps import forms
from apps.forms import AppForm1,AppForm2,AppForm3,AppForm,FlurryForm,ParseForm
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect,Http404
from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.core.context_processors import request
from django.core import serializers, urlresolvers
from django.core.urlresolvers import reverse
import json 
from django.views.defaults import shortcut
from django import shortcuts
from django.shortcuts import render_to_response
import cgi
import cgitb
import sys
from urllib2 import urlopen
import urllib
import urllib2
from django.utils import simplejson as json
import pprint
from django.contrib import messages
from platforms.models import Flurry

# Register your models here.
class AppAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['name','pub_date','category','description','playstore_url','itunes_url','platforms','devices','plugins']}),
#         
#     ]
    
#     inlines = [ApInline]
    list_filter = ['pub_date']
    list_display = ('name', 'category','playstore_url','itunes_url')
#     change_list_template = 'admin/app_settings.html'
    change_form_template='admin/advanced.html'
#     search_fields = ['question']
    def get_urls(self):
            urls = super(AppAdmin, self).get_urls()
            print urls
            print "ali"
            my_urls = patterns('',
                               url(r'^add/$', self.admin_site.admin_view(self.create_app_wizard), name="appwizard"),
                               url(r'^step1/$', self.admin_site.admin_view(self.step1), name="wizard_step1"),
                               url(r'^step2/$', self.admin_site.admin_view(self.step2), name="wizard_step2"),
                               url(r'^step3/$', self.admin_site.admin_view(self.step3), name="wizard_step3"),
                               url(r'^appajax4/$', self.admin_site.admin_view(self.appajax4), name="appajax4"),
                               
                               
                               url(r'^dashboard/$', self.admin_site.admin_view(self.dashboard), name="app-dashboard"),
                               url(r'^advancedSettings/(?P<id>[\w-]+)/$', self.admin_site.admin_view(self.advancedSettings), name="advancedSettings"),
                               )
            my_urls = my_urls + urls
         
            return my_urls
        
    # wizard start loading
    def create_app_wizard(self, request,extra_context=None):
        appform1=AppForm1
        appform2=AppForm2
        appform3=AppForm3
        return render(request,'admin/wizard.html',{'appform1':appform1,'appform2':appform2,'appform3':appform3})
    

    #step1
    def step1(self,request):
        appform1=AppForm1()
        if request.is_ajax():
            
            appform1=AppForm1(request.POST)
            if appform1.is_valid():
                return render_to_response("admin/partials/wizardform1.html",{'appform1':appform1} )
            else: 
                return render_to_response("admin/partials/wizardform1.html",{'appform1':appform1} )
    #step2
    def step2(self,request):
        
        appform2=AppForm2()
        if request.is_ajax():
            
            appform2=AppForm2(request.POST)
            if appform2.is_valid():
#                 if appform2.save():
                    
                    return render_to_response("admin/partials/wizardform2.html",{'appform2':appform2}) 
            else:    
                    return render_to_response("admin/partials/wizardform2.html",{'appform2':appform2}) 
    
        return render_to_response("admin/partials/wizardform2.html",{'appform2':appform2})
   
    #step3           
    def step3(self,request):
  
        appform3=AppForm3()
        
        if request.is_ajax():
            form=AppForm(request.POST)
            if form.is_valid():
                
                if  form.save(request) :
                    messages.success(request,'You App is Created !')
                    return render_to_response("admin/partials/wizardform3.html",{'appform3':appform3 })
                else:
                    return render_to_response("admin/partials/wizardform3.html",{'appform3':appform3 })
            return render_to_response("admin/partials/wizardform3.html",{'appform3':appform3})    
        


    def queryset(self, request):
        qs = super(AppAdmin, self).queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(create_user=request.user)
        return qs
    
    def dashboard(self,request):
        url="http://api.flurry.com/eventMetrics/Summary?apiAccessCode=G27F3VNNPWN5KF67H8FZ&apiKey=ZXQFP56DZF8DFGSZSQCV&startDate=2013-10-10&endDate=2014-03-13&country=ALL"
        totalcount=''
        totalsession=''
        file = urllib.urlopen(url)
        content = file.read()
        content = json.loads(content)
        for key,value in content['event'].iteritems():
            if key=='@totalCount':
                totalcount=value    
            if key=='@totalSessions':
                totalsession=value    
        
        app = App.objects.all()
        return render_to_response("admin/page.html",{'app':app,'downloads':totalcount,'sessions':totalsession})
    def advancedSettings(self,request,id,context=None):
#             actions = self.get_actions(request)
#        
#             action_form = None
        return super(AppAdmin, self).change_view(request, id, extra_context=None)
    
    def appajax4(self,request):
        flurry=FlurryForm
        parse=ParseForm
        print flurry.as_p
        return render_to_response("admin/partials/app_settings.html",{'flurry':flurry,'parse':parse} )
#         if request.is_ajax():
#              
#             flurry=FlurryForm(request.POST)
#             if flurry.is_valid():
#                 return render_to_response("admin/partials/app_settings.html",{'flurry':flurry} )
#     
# #                 appform1.empty_permitted
# #                 if appform1.save():
# #                     return render_to_response("admin/page.html") 
#             else: 
               
  
#         print appid
#         app=App.objects.all(
#                                   {'app' : app})
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

