from django.contrib import admin
from .models import blog,topic
# Register your models here.

class listdisplay(admin.ModelAdmin):
    list_display = ('slug','date','topicname')

admin.site.register(blog,listdisplay)
admin.site.register(topic)