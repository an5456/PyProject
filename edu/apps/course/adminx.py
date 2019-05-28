
from django.contrib import admin
from . import models
import xadmin

class CourseAdmin(object):

    list_display = ('user','teacher', 'level','title','content','cost', 'status')
    list_filter = ['user','teacher', 'level','title','content','cost', 'status']
    search_fields = ['user','teacher', 'level','title','content','cost', 'status']
    model_icon = 'fa fa-home'

class CatLogAdmin(object):

    list_display = ('title','label', 'class_type','capter','Course','type', 'status')
    list_filter = ['title','label', 'class_type','capter','Course','type', 'status']
    search_fields = ['title','label', 'class_type','capter','Course','type', 'status']
    model_icon = 'fa fa-square'

class ObjectAdmin(object):

    list_display = ('title','Course', 'pic','content')
    list_filter = ['title','Course', 'pic','content']
    search_fields = ['title','Course', 'pic','content']
    model_icon = 'fa fa-cog'

class VideoAdmin(object):

    list_display = ('Catalog','over_time', 'video')
    list_filter = ['Catalog','over_time', 'video']
    search_fields = ['Catalog','over_time', 'video']
    model_icon = 'fa fa-pencil'

class UserCourseAdmin(object):

    list_display = ('user','course', 'status','dopercent')
    list_filter = ['user','course', 'status','dopercent']
    search_fields = ['user','course', 'status','dopercent']
    model_icon = 'fa fa-book'


xadmin.site.register(models.Course, CourseAdmin)

xadmin.site.register(models.Catalog, CatLogAdmin)

xadmin.site.register(models.Object, ObjectAdmin)

xadmin.site.register(models.Video, VideoAdmin)

xadmin.site.register(models.UserCourse, UserCourseAdmin)