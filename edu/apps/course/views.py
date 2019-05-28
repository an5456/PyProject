from django.shortcuts import render
from .forms import updatetaskForm,playForm
# Create your views here.
import json
import datetime
from django.http import HttpResponse
from .models import Course
from .models import Catalog
from .models import UserCourse
from user.models import User
from task.models import Task
from django.conf import settings
from django.forms.models import model_to_dict

# 这里是一个json的扩展用于格式化日期对象，如更新和新建数据日期
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

# 单个课程的主页，也就是课程介绍页面
def index(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not "id" in json.loads(request.body)['params'] or json.loads(request.body)['params']['id'] == '':
            message = {'code': 2001, 'detail': '缺少课程id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
        params = json.loads(request.body)['params']
        
        # 通过id获取课程
        course = Course.objects.filter(id=params['id'])
        # 通过课程获取目录
        catalogs = course[0].catalog_set.all()
        catalogs = list(catalogs.values())
        newcatalogs=[]
        # 将节放在所属章下面
        for catalog in catalogs:
            if catalog['type']=='chapter':
                sections=[]
                for section in catalogs:
                    if section['capter_id']==catalog['id'] and section['type']=='section':
                        sections.append(section)
                catalog['sections']=sections
                newcatalogs.append(catalog)
        # 获取该课程项目列表
        objects = course[0].object_set.all()
        objects = list(objects.values())
        objectvalues = []
        # 处理静态资源前缀
        for object in objects:
            object['pic'] =  settings.STATIC_URL_PRE + object['pic']
            objectvalues.append(object)
        
        # 该课程老师列表
        teachers = course[0].teacher.all()
        teachers = list(teachers.values())
        course = list(course.values())
        course[0]['teachers'] = teachers
        course[0]['objects'] = objects

        course[0]['catalogs'] = newcatalogs
        course[0]['pic'] = settings.STATIC_URL_PRE + course[0]['pic']
        message = {}
        message["course"]=course
        # 返回json
        return HttpResponse(json.dumps(message, ensure_ascii=False,cls=DateEncoder), content_type="application/json")

# 获取付款信息列表
def getpayinfo(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not "id" in json.loads(request.body)['params'] or json.loads(request.body)['params']['id'] == '':
            message = {'code': 2001, 'detail': '缺少课程id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
        params = json.loads(request.body)['params']
        # 通过课程id获取课程名和价格
        course = Course.objects.values('title','cost').get(id=params['id']);
        message = {}
        message["course"]=course
        return HttpResponse(json.dumps(message, ensure_ascii=False,cls=DateEncoder), content_type="application/json")

# 获取目录列表，主要用于单独列出目录的情况如播放列表
def cataloglist(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not "id" in json.loads(request.body)['params'] or json.loads(request.body)['params']['id'] == '':
            message = {'code': 2001, 'detail': '缺少课程id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
        params = json.loads(request.body)['params']
        course = Course.objects.filter(id=params['id'])
        catalogs = course[0].catalog_set.all()
        catalogvalues = []
        for catalog in catalogs:
            # 处理视频url
            video = catalog.video_set.all()
            catalog = model_to_dict(catalog)
            if not len(list(video)) == 0:
                video = model_to_dict(list(video)[0])
                video['video'] =  settings.STATIC_URL_PRE+video['video'].url
                catalog['video'] = video

            catalogvalues.append(catalog)

        course = list(course.values())
        course[0]['catalogs'] = catalogvalues
        message = {}
        message["course"] = course
        return HttpResponse(json.dumps(message, ensure_ascii=False,cls=DateEncoder), content_type="application/json")

# 获取目录列表，主要用于单独列出目录的情况如播放列表，这个带这个人的所有目录任务进行情况如，某个人看了多长时间，是否已完成
def videolist(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not "courseid" in json.loads(request.body)['params'] or json.loads(request.body)['params']['courseid'] == '' or not "userid" in json.loads(request.body)['params'] or json.loads(request.body)['params']['userid'] == '':
            message = {'code': 2001, 'detail': '缺少课程id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
        params = json.loads(request.body)['params']
        course = Course.objects.filter(id=params['courseid'])
        user = User.objects.get(id=params['userid'])
        catalogs = course[0].catalog_set.all()
        catalogvalues = []
        for catalog in catalogs:
            catalogdic = model_to_dict(catalog)

            video = catalog.video_set.all()
            if not len(list(video)) == 0:
                video = model_to_dict(list(video)[0])
                video['video'] =  settings.STATIC_URL_PRE + video['video'].url
                catalogdic['video'] = video
            # 上面处理和之前的目录列表方法一样，只有这里加入了任务情况
            task = catalog.task_set.filter(user=user).values()
            if not len(list(task)) == 0:
                task=list(task)[0]
                catalogdic['task'] = task

            catalogvalues.append(catalogdic)

        course = {}
        course['catalogs'] = catalogvalues
        return HttpResponse(json.dumps(course, ensure_ascii=False,cls=DateEncoder), content_type="application/json")

# 获取目录列表，主要用于单独列出目录的情况如播放列表，这个带这个人的所有目录任务进行情况如，某个人看了多长时间，是否已完成
def play(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not playForm(
                json.loads(request.body)['params']).is_valid():
            message = {'code': 2001, 'detail': '缺少课程id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
        params = json.loads(request.body)['params']
        course = Course.objects.filter(id=params['courseid'])
        user = User.objects.get(id=params['userid'])
        catalogs = course[0].catalog_set.all()
        catalogvalues = []
        for catalog in catalogs:
            catalogdic = model_to_dict(catalog)

            video = catalog.video_set.all()
            if not len(list(video)) == 0:
                video = model_to_dict(list(video)[0])
                video['video'] =  settings.STATIC_URL_PRE + video['video'].url
                catalogdic['video'] = video
            # 上面处理和之前的目录列表方法一样，只有这里加入了任务情况
            task = catalog.task_set.filter(user=user).values()
            if not len(list(task)) == 0:
                task=list(task)[0]
                catalogdic['task'] = task

            catalogvalues.append(catalogdic)

        course = {}
        course['catalogs'] = catalogvalues
        # 通过id获取目录和视频
        catalogs = Catalog.objects.filter(id=params['catalogid'])
        catalogvalues = []

        for catalog in catalogs:
            catalogdic = model_to_dict(catalog)

            video = catalog.video_set.all()
            if not len(list(video)) == 0:
                video = model_to_dict(list(video)[0])
                video['video'] = settings.STATIC_URL_PRE + video['video'].url
                catalogdic['video'] = video
            catalogvalues.append(catalogdic)
        course['video'] = catalogvalues
        return HttpResponse(json.dumps(course, ensure_ascii=False,cls=DateEncoder), content_type="application/json")



# 获取单独列表数据用于播放
def getcatalog(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not "catalogid" in json.loads(request.body)['params'] or \
                json.loads(request.body)['params']['catalogid'] == '':
            message = {'code': 2001, 'detail': '缺少目录id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
        params = json.loads(request.body)['params']
        # 通过id获取目录和视频
        catalogs = Catalog.objects.filter(id=params['catalogid'])
        catalogvalues = []

        for catalog in catalogs:
            catalogdic = model_to_dict(catalog)

            video = catalog.video_set.all()
            if not len(list(video)) == 0:
                video = model_to_dict(list(video)[0])
                video['video'] = settings.STATIC_URL_PRE + video['video'].url
                catalogdic['video'] = video

            # task = catalog.task_set.all()
            # if not len(list(task)) == 0:
            #     task = model_to_dict(list(task)[0])
            #     catalogdic['task'] = task

            catalogvalues.append(catalogdic)

        course = {}
        course['catalog'] = catalogvalues
        return HttpResponse(json.dumps(course, ensure_ascii=False, cls=DateEncoder),
                            content_type="application/json")



# 获取用户的course状态
def getusercourse(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not "courseid" in json.loads(request.body)['params'] or json.loads(request.body)['params']['courseid'] == '' or not "userid" in json.loads(request.body)['params'] or json.loads(request.body)['params']['userid'] == '':
            message = {'code': 2001, 'detail': '缺少课程id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
        params = json.loads(request.body)['params']
        course = Course.objects.filter(id=params['courseid'])
        user = User.objects.get(id=params['userid'])
        catalogs = course[0].catalog_set.all()
        catalogvalues = []
        nextcatalog = {}
        # 完成任务量
        overnum=0
        for catalog in catalogs:
            catalogdic = model_to_dict(catalog)

            video = catalog.video_set.all()
            if not len(list(video)) == 0:
                video = model_to_dict(list(video)[0])
                video['video'] =  settings.STATIC_URL_PRE + video['video'].url
                catalogdic['video'] = video
                # 这里加入了任务情况,没有任务说明任务未开始，即是下一个任务
                task = catalog.task_set.filter(user=user).values()
                if not len(list(task)) == 0:
                    task=list(task)[0]
                    # 统计完成任务量
                    if task['status'] == 'over':
                        overnum += 1
                    elif not nextcatalog:
                        nextcatalog['id'] = catalog.id
                        nextcatalog['title'] = catalog.title
                    catalogdic['task'] = task
                # 任务未开始，并且下一个任务列表未空记录为下一个
                elif not nextcatalog:
                    nextcatalog['id'] = catalog.id
                    nextcatalog['title'] = catalog.title
            catalogvalues.append(catalogdic)
        catalogs = course[0].catalog_set.all()
        catalogs = list(catalogs.values())
        newcatalogs = []
        # 任务数
        tasknum = 0
        dopercent = 0
        # 将节放在所属章下面
        for catalog in catalogs:
            if catalog['label'] == "start":
                catalog['label'] = "基础知识"
            elif catalog['label'] == "startandproject":
                catalog['label'] = "基础知识和项目实践班"
            else:
                catalog['label'] = " "
            if catalog['type'] == 'chapter':
                sections = []
                for section in catalogs:
                    # 记录所有任务数
                    if section['capter_id'] == catalog['id'] and section['type'] == 'section':
                        tasknum += 1
                        sections.append(section)
                catalog['sections'] = sections
                newcatalogs.append(catalog)

        # 这里判断是判断分母不可为0
        usercourse = UserCourse.objects.filter(user=user, course=course[0])
        dopercent = model_to_dict(list(usercourse)[0])['dopercent']

        course=list(course.values('id', 'title', 'live_time'))[0]
        course['dopercent']=dopercent
        ref = {}

        ref['course'] = course
        ref['tasknum'] = tasknum
        ref['overnum'] = overnum
        ref['nextcatalog'] = nextcatalog
        ref['catalogs'] = newcatalogs
        return HttpResponse(json.dumps(ref, ensure_ascii=False,cls=DateEncoder), content_type="application/json")



# 更新任务状态（某个人完成了多长时间的视频观看，是否已全部完成，没有记录就新建）
def updatetask(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not updatetaskForm(json.loads(request.body)['params']).is_valid():
            message = {'code': 2001, 'detail': '缺少参数！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

        params = json.loads(request.body)['params']

        # 获取相对任务的目录和用户
        catalog = Catalog.objects.get(id=params['catalogid'])
        user = User.objects.get(id=params['userid'])
        # 获取目录相对课程
        course = catalog.Course

        # 如果这个用户还没有进行这个目录的任务就新建
        if not Task.objects.filter(user=user, catlog=catalog):
            Task.objects.create(user=user, catlog=catalog, do_time="0", status="unover")

        catalogs = Catalog.objects.filter(id=params['catalogid'])
        dotime = params['dotime']
        catalogvalues = []

       
        for catalog in catalogs:
            catalogdic = model_to_dict(catalog)

            video = catalog.video_set.all()
            # 如果这个目录是个视频目录
            if not len(list(video)) == 0:
                video = model_to_dict(list(video)[0])
                video['video'] = settings.STATIC_URL_PRE + video['video'].url
                catalogdic['video'] = video
            task = catalog.task_set.filter(user=user)
            if not len(list(task)) == 0:
                task = model_to_dict(list(task)[0])
                catalogdic['task'] = task

            catalogvalues.append(catalogdic)
         # 如果已经在里面，就更新，完成时间如果比正常时间减2分钟大就更新为已完成
        if 'video' in catalogvalues[0]:
            if float(catalogvalues[0]['video']['over_time']) - 2 < float(dotime):
                task = Task.objects.get(id=catalogvalues[0]['task']['id'])
                task.do_time = dotime
                task.status = 'over'
                task.save()
            else:
                task = Task.objects.get(id=catalogvalues[0]['task']['id'])
                task.do_time = dotime
                task.save()


        # 从新计算完成度
        catalogs = list(course.catalog_set.filter(type="section").values())
        overnum = 0
        for catalog in catalogs:
            if len(Task.objects.filter(catlog=catalog['id'],user=user,status="over")):
                overnum += 1
        if len(catalogs):
            dopercent = int(round(overnum / len(catalogs), 2) * 100)
            usercourse = UserCourse.objects.get(user=user,course=course)
            usercourse.dopercent = dopercent
            usercourse.save()

        message = {'code': 2000, 'detail': '更新任务状态成功！'}
        return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

# 该方法已废弃，用于新建task
def addtask(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not updatetaskForm(json.loads(request.body)['params']).is_valid():
            message = {'code': 2001, 'detail': '缺少参数！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

        params = json.loads(request.body)['params']
        catalog = Catalog.objects.get(id=params['catalogid'])
        user = User.objects.get(id=params['userid'])
        Task.objects.create(user=user,catalog=catalog,dotime="0",status="unover")

        message = {'code': 2000, 'detail': '新建任务成功！'}
        return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")