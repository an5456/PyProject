from django.db import models

# Create your models here.
class Banner(models.Model):
    '''banner图表'''



    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128,null=True,verbose_name="标题")
    pic = models.FileField(upload_to='upload/pic/banner/%Y/%m/%d',verbose_name="图片",null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "banner"
        ordering = ['id']
        verbose_name = 'banner图'
        verbose_name_plural = 'banner图'