
from django.contrib import admin
from . import models
import xadmin

class OrderAdmin(object):

    list_display = ('user','course', 'usercourse','total_amount','discount','pay_method', 'status')
    list_filter = ['user','course', 'usercourse','total_amount','discount','pay_method', 'status']
    search_fields = ['user','course', 'usercourse','total_amount','discount','pay_method', 'status']
    model_icon = 'fa fa-home'


xadmin.site.register(models.Order, OrderAdmin)

