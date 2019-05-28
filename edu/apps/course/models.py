from django.db import models
 
class Course(models.Model):
    '''课程表'''
    
    status_gender = (
        ('public','已发布'),
        ('unpublic','未发布'),
    )
    stick_gender = (
        ('stick', '置顶'),
        ('unstick', '未置顶'),
    )
    level_gender = (
        ('training','精品'),
        ('heigh','高级'),
        ('start','基础')
    )

    user = models.ManyToManyField('user.User', through='UserCourse',
                                  through_fields=('course', 'user'))

    pic = models.FileField(upload_to='upload/pic/course/%Y/%m/%d',null=True)
    teacher = models.ManyToManyField('teacher.teacher')
    status = models.CharField(max_length=32,choices=status_gender,default='未发布',verbose_name="课程状态")
    level = models.CharField(max_length=32,choices=level_gender,default='免费',verbose_name="课程类别")
    stick = models.CharField(max_length=32, choices=stick_gender, default='未置顶',verbose_name="是否推荐")
    id=models.AutoField(primary_key=True)
    max_people_num=models.IntegerField(default=0,verbose_name="最多人数")
    cost=models.IntegerField(default=0,verbose_name="价钱")
    title = models.CharField(max_length=128,verbose_name="标题")

    url = models.CharField(max_length=128,null=True,verbose_name="课程页面url")
    content = models.CharField(max_length=500,verbose_name="内容描述")
    live_time = models.DateTimeField(verbose_name="学习有效期",null=True)
    last_time = models.DateTimeField(verbose_name="上次开课时间")

    next_time = models.DateTimeField(verbose_name="下次开课时间")
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title
 
    class Meta:
        db_table = "course"
        ordering = ['c_time']
        verbose_name = '课程'
        verbose_name_plural = '课程'


class Object(models.Model):
    '''项目表'''


    Course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name="所属课程")
    id = models.AutoField(primary_key=True)
    pic = models.FileField(upload_to='upload/pic/object/%Y/%m/%d', null=True,verbose_name="图片")
    title = models.CharField(max_length=128,verbose_name="标题")
    content = models.CharField(max_length=500,verbose_name="内容")
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "object"
        ordering = ['c_time']
        verbose_name = '项目'
        verbose_name_plural = '项目'


class Catalog(models.Model):
    '''目录表'''
    
    class_type_gender = (
        ('video','视频'),
        ('question','问题'),
        ('article','文章'),
        ('data','资料'),
    )
    type_gender = (
        ('chapter','章'),
        ('section','节'),
    )
    isproject_gender = (
        ('yes', '是'),
        ('no', '否'),
    )
    status_gender = (
        ('public','已发布'),
        ('unpublic','未发布'),
    )

    label_gender = (
        ('start', '基础知识'),
        ('startandproject', '基础和项目实践')
    )
    label = models.CharField(max_length=32, choices=label_gender, default='基础知识', verbose_name="章节标签")
    content = models.CharField(max_length=256, null=True, verbose_name="章节内容描述")
    class_type = models.CharField(max_length=32,choices=class_type_gender,default='视频')
    isproject = models.CharField(max_length=32, choices=isproject_gender, default='是否是项目')
    capter = models.ForeignKey('self',on_delete=models.PROTECT, verbose_name="所属章节",null=True,blank=True)
    Course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name="课程")
    status = models.CharField(max_length=32,choices=status_gender,default='未发布')
    type = models.CharField(max_length=32,choices=type_gender,default='节')
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=128,verbose_name="标题")
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title
 
    class Meta:
        db_table = "catalog"
        ordering = ['c_time']
        verbose_name = '目录'
        verbose_name_plural = '目录'

class Video(models.Model):
    '''视频表'''

    id=models.AutoField(primary_key=True)
    Catalog = models.ForeignKey('Catalog', on_delete=models.PROTECT, null=True, verbose_name="目录项")
    over_time = models.CharField(max_length=128,verbose_name="完成最短用时")
    video = models.FileField(upload_to='upload/video/course/%Y/%m/%d', null=True,verbose_name="视频")
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = "video"
        ordering = ['c_time']
        verbose_name = '视频'
        verbose_name_plural = '视频'

class UserCourse(models.Model):
    '''用户学习课程表'''

    gender = (
        ('open', '开放'),
        ('close', '关闭'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User',on_delete=models.PROTECT,null=True, verbose_name="用户")
    course = models.ForeignKey('Course',on_delete=models.PROTECT,null=True, verbose_name="课程")
    status = models.CharField(max_length=32,choices=gender,default='open')
    dopercent = models.CharField(max_length=32,default='0',verbose_name="完成度")
    c_time = models.DateTimeField(auto_now_add=True,verbose_name="加入时间")

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = "usercourse"
        ordering = ['c_time']
        verbose_name = '用户课程'
        verbose_name_plural = '用户课程'