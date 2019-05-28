
from django.contrib import admin
from . import models
import xadmin

class TaskAdmin(object):

    list_display = ('user','do_time', 'catlog','status')
    list_filter = ['user','do_time', 'catlog','status']
    search_fields = ['user','do_time', 'catlog','status']
    model_icon = 'fa fa-home'


xadmin.site.register(models.Task, TaskAdmin)

