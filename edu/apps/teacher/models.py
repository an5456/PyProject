from django.db import models


# Create your models here.
class teacher(models.Model):
    '''老师表'''
    
    stick_gender = (
        ('stick', '置顶'),
        ('unstick', '未置顶'),
    )

    stick = models.CharField(max_length=32, choices=stick_gender, default='未置顶',verbose_name="是否推荐")
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=128,verbose_name="是否姓名")
    label = models.CharField(max_length=128,verbose_name="头衔")
    content = models.CharField(max_length=500,verbose_name="简介1")
    content2 = models.CharField(max_length=500,verbose_name="简介2",null=True)
    user = models.OneToOneField('user.User',verbose_name="关联用户",null=True,on_delete=models.PROTECT)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name

    class Meta:
        db_table="teacher"
        ordering = ['c_time']
        verbose_name = '老师'
        verbose_name_plural = '老师'
