from django.db import models


# Create your models here.
class Task(models.Model):
    '''任务表'''

    status_gender = (
        ('over', '已完成'),
        ('unover', '未完成'),
    )

    status = models.CharField(max_length=32, choices=status_gender, default='未完成')
    catlog = models.ForeignKey('course.Catalog', on_delete=models.PROTECT, null=True, verbose_name="目录")
    user = models.ForeignKey('user.User', on_delete=models.PROTECT, null=True, verbose_name="用户")
    id = models.AutoField(primary_key=True)
    do_time = models.CharField(max_length=128,verbose_name="完成时间")
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = "task"
        ordering = ['c_time']
        verbose_name = '任务'
        verbose_name_plural = '任务'
