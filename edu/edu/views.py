# index/views.py

from django.http import HttpResponse
from course.models import Course
from teacher.models import teacher
from django.conf import settings
import json
import datetime

# 这里是一个json的扩展用于格式化日期对象，如更新和新建数据日期
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

# 主页信息
def index(request):
    if request.method == "POST":
        # 精品课
        trainingcourses=Course.objects.filter(level="training",stick='stick')
        # 高级课
        heighcourses = Course.objects.filter(level="heigh",stick='stick')
        # 初级课
        startcourses = Course.objects.filter(level="start",stick='stick')
        # 首页老师
        teachers = teacher.objects.filter(stick='stick')
        trainingcourses = list(trainingcourses.values())
        heighcourses = list(heighcourses.values())
        startcourses = list(startcourses.values())
        # 处理课程的图片加上配置文件中的url前缀
        for course in startcourses:
            course['level']='初级'
            print(course['pic'])
            if not course['pic']==None:
                course['pic'] = settings.STATIC_URL_PRE + course['pic']
        for course in heighcourses:
            course['level'] = '高级'
            if not course['pic']==None:
                course['pic'] = settings.STATIC_URL_PRE + course['pic']
        for course in trainingcourses:
            course['level'] = '训练营'
            if not course['pic']==None:
                course['pic'] = settings.STATIC_URL_PRE + course['pic']
        teachers = list(teachers.values())
        message = {}
        message["trainingcourses"] = trainingcourses
        message["heighcourses"] = heighcourses
        message["startcourses"] = startcourses
        message["teachers"] = teachers
        # 返回json
        return HttpResponse(json.dumps(message, ensure_ascii=False,cls=DateEncoder), content_type="application/json")


