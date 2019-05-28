
from django.contrib import admin
from . import models
import xadmin

class BannerAdmin(object):

    list_display = ('title','pic')
    list_filter = ['title','pic']
    search_fields = ['title','pic']
    model_icon = 'fa fa-home'

xadmin.site.register(models.Banner, BannerAdmin)

