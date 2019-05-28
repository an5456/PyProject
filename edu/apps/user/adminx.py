__author__ = "zhou"
__date__ = "2019-04-04 11:38"

from django.contrib import admin
from . import models
import xadmin

class UserAdmin(object):

    list_display = ('realname', 'nickname', 'telphone', 'email')
    list_filter = ['realname', 'nickname', 'telphone', 'email']
    search_fields = ['realname', 'nickname', 'telphone', 'email']
    model_icon = 'fa fa-home'

xadmin.site.register(models.User, UserAdmin)

