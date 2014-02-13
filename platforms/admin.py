from django.contrib import admin
from platforms.models import Platform,Plugin,Flurry,GoogleAnalytics,Parse,UrbanAirship,Facebook
# Register your models here.
class PlatformAdmin(admin.ModelAdmin):
        pass
class PluginAdmin(admin.ModelAdmin):
        pass
class FlurryAdmin(admin.ModelAdmin):
        pass
class GoogleAnalyticsAdmin(admin.ModelAdmin):
        pass
class ParseAdmin(admin.ModelAdmin):
        pass
class UrbanAirshipAdmin(admin.ModelAdmin):
        pass
class FacebookAdmin(admin.ModelAdmin):
        pass
    




admin.site.register(Platform, PlatformAdmin)
admin.site.register(Facebook,FacebookAdmin )
admin.site.register(Flurry,FlurryAdmin )
admin.site.register(GoogleAnalytics,GoogleAnalyticsAdmin )
admin.site.register(Parse,ParseAdmin )
admin.site.register(Plugin,PluginAdmin )
admin.site.register(UrbanAirship,UrbanAirshipAdmin )
