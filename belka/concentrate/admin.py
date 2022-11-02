from django.contrib import admin

# Register your models here.
from concentrate.models import Concentrate, Month


class ConcentrateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'iron', 'silicon', 'aluminum', 'calcium', 'sulfur', 'month')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class MonthAdmin(admin.ModelAdmin):
    list_display = ('id', 'month')
    list_display_links = ('id', 'month')
    search_fields = ('month',)


admin.site.register(Concentrate, ConcentrateAdmin)
admin.site.register(Month, MonthAdmin)
