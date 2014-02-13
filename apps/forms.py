

from django import forms
from apps.models import App
from platforms.models import Platform,Plugin
from django.contrib.admin.widgets import FilteredSelectMultiple
    
class AppForm1(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'icon','description']
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
    class Meta:
        model = Plugin
        widgets = {
                'name' : forms.CheckboxSelectMultiple,
                
            }
        
        fields = ['name']