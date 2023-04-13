from django.contrib import admin

from .models import *

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)


admin.site.register(Characteristic, CharacteristicAdmin)

admin.site.site_title = 'Administration panel'
admin.site.site_header = 'PIE app owner'
