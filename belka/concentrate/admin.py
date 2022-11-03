from django.contrib import admin

# Register your models here.
from concentrate.models import Concentrate


class ConcentrateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'iron', 'silicon', 'aluminum', 'calcium', 'sulfur', 'month')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Concentrate, ConcentrateAdmin)

