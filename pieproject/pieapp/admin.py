from django.contrib import admin

from .models import *

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Characteristic, CharacteristicAdmin)

admin.site.site_title = 'Administration panel'
admin.site.site_header = 'Administration'
