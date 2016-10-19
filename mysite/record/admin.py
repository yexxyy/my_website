from django.contrib import admin
from models import *


class ChoiceInline(admin.TabularInline):
    model = RecordImg
    extra = 1


class RecordAdmin(admin.ModelAdmin):

    inlines = [ChoiceInline]

    #list_display = ('question_text','pub_date','was_publisthed_recently')
    #$list_filter = ['pub_date']
    #search_fields = ['question_text']




admin.site.register(Record,RecordAdmin)
admin.site.register(RecordImg)