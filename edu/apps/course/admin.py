from django.contrib import admin

# Register your models here.
from . import models
 
admin.site.register(models.Course)
admin.site.register(models.Catalog)
admin.site.register(models.Video)
admin.site.register(models.Object)
admin.site.register(models.UserCourse)