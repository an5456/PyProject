from django.db import models
 
class User(models.Model):
    '''用户表'''
 
    gender = (
        ('male','男'),
        ('female','女'),
    )

    pic = models.FileField(upload_to='upload/pic/user/%Y/%m/%d', null=True,verbose_name="用户图片")
    realname = models.CharField(max_length=128,null=True,unique=True,verbose_name="真实姓名")
    nickname = models.CharField(max_length=128,null=True,unique=True,verbose_name="昵称")
    paypassword = models.CharField(max_length=128, null=True, unique=True,verbose_name="支付密码")
    telphone = models.CharField(max_length=128, null=True, unique=True,verbose_name="电话")
    password = models.CharField(max_length=256,verbose_name="密码")
    email = models.EmailField(unique=True,verbose_name="邮箱")
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.nickname if self.nickname else "null"

    class Meta:
        db_table = "user"
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
