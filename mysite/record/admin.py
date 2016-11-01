# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *



class ChoiceInline(admin.TabularInline):
    model = RecordImg
    extra = 1

class RecordAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class ContactDataAdmin(admin.ModelAdmin):

    list_display = ['name','phone','mail','message']
    search_fields = ['name']



admin.site.register(Record,RecordAdmin)
#admin.site.register(RecordImg)
admin.site.register(ContactData,ContactDataAdmin)