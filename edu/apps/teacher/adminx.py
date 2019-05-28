
from django.contrib import admin
from . import models
import xadmin

class TeacherAdmin(object):

    list_display = ('name',  'user','label', 'content','content2')
    list_filter = ['name',  'user','label', 'content','content2']
    search_fields = ['name',  'user','label', 'content','content2']
    model_icon = 'fa fa-home'


xadmin.site.register(models.teacher, TeacherAdmin)

