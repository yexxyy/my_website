from django.contrib import admin
from models import *



class ChoiceInline(admin.TabularInline):
    model = RecordImg
    extra = 1
class RecordAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]



admin.site.register(Record,RecordAdmin)
admin.site.register(RecordImg)