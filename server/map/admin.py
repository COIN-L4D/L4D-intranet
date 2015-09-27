from django.contrib import admin

from .models import MapSettings, MapEvent

class MapSettingsAdmin(admin.ModelAdmin):
    pass

class MapEventAdmin(admin.ModelAdmin):
    pass

admin.site.register(MapSettings, MapSettingsAdmin)
admin.site.register(MapEvent, MapEventAdmin)
