

from django import forms
from apps.models import App, AppPlugin
from platforms.models import Platform,Plugin,AppPlatform
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models.base import Model
from time import timezone

class PlatformForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = ['name']
class AppForm1(forms.ModelForm):
    
    class Meta:
        model = App
        fields = ['name','description']
    def __init__(self, *args, **kwargs):
        super(AppForm1, self).__init__(*args, **kwargs)
        #setting errors

        for f in self.errors:
            self.fields[f].widget.attrs.update({'class': 'error'})
#         fields = ['name', 'description']
class AppForm2(forms.ModelForm):
#    forms.ModelMultipleChoiceField(queryset=Platform.objects.all(), widget=FilteredSelectMultiple("verbose name", is_stacked=False))
    

    class Meta:
          
            
        widgets = {
                'platforms' : forms.CheckboxSelectMultiple,
                'devices' :forms.CheckboxSelectMultiple
            }
            
        model = App
        fields = ['category','platforms', 'devices','playstore_url','itunes_url']
#     def __init__(self, *args, **kwargs):
#         super(AppForm2, self).__init__(*args, **kwargs)

#         self.fields['platforms'].widget = forms.CheckboxSelectMultiple()
class AppForm3(forms.ModelForm):
#     plugin=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Plugin.objects.all(), required=False)
    class Meta:
        widgets = {
                'plugins' : forms.CheckboxSelectMultiple,
            }
        model = App
        fields = ['plugins']
class AppForm(forms.ModelForm):
    
    class Meta:
        model=App  
       
        fields=['name','description','category','platforms', 'devices','playstore_url','itunes_url','plugins']
 
    def save(self, *args, **kw):
#           commentModel.content_type_id = 47
#         commentModel.object_pk = self.cleaned_data.get("object_pk")
#         commentModel.site_id = 1
#         commentModel.user_id = self.request.user.id
#         commentModel.user_name = self.cleaned_data.get("user_name")
#         commentModel.user_email = self.cleaned_data.get("user_email")
#         commentModel.user_url = self.cleaned_data.get("user_url")
#         commentModel.submit_date = datetime.datetime.today()
#         commentModel.comment = self.cleaned_data.get("comment")
#         commentModel.ip_address = socket.gethostbyname(socket.gethostname())
#         commentModel.save()
        
        instance = App()
        instance.name = self.cleaned_data.get('name')
        instance.description = self.cleaned_data.get('description')
        instance.category = self.cleaned_data.get('category')
        
#         instance.platforms = self.cleaned_data.get('platforms')
#         instance.devices = self.cleaned_data.get('devices')
        instance.playstore_url = self.cleaned_data.get('playstore_url')
        instance.itunes_url = self.cleaned_data.get('itunes_url')
#         instance.plugins = self.cleaned_data.get('plugins')
#         print instance.name
#        instance.save()
    
        instance.save()
      
        for key in self.cleaned_data['platforms']:
                instance.platforms.add(key)
        for key in self.cleaned_data['devices']:
                instance.devices.add(key)
        for key in self.cleaned_data['plugins']:
                instance.plugins.add(key)
                
                return True;

          



#     def __init__(self, qs=None, *args, **kwargs):
#         super(App, self).__init__(*args, **kwargs)
#         if qs:
#             self.fields['plugins']=forms.ModelMultipleChoiceField(choices=Plugin.objects.all(),widget=forms.CheckboxSelectMultiple())
        
#         widgets = {
#                 'plugins' : forms.ModelMultipleChoiceField(choices=Plugin.objects.all(),widget=forms.CheckboxSelectMultiple()),
#                 
#             }
#     def __init__(self, qs=None, *args, **kwargs):
#         super(App, self).__init__(*args, **kwargs)
#         if qs:
#             self.fields['plugins']=forms.ModelMultipleChoiceField(choices=Plugin.objects.all(),widget=forms.CheckboxSelectMultiple())
        