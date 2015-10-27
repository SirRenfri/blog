from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
   list_display = ('title','date','text')
   list_filter = ('date',)
   search_fields = ['title', 'text']
   date_hierarchy = 'date'
   ordering = ('date',)

admin.site.register(Message, MessageAdmin)
