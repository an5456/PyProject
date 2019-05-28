# user/views.py
 
from django.shortcuts import render,redirect
from . import models
from django.conf import settings
from django.core.cache import cache
from course.models import UserCourse
from django.forms.models import model_to_dict

from django.http import HttpResponse
from .forms import UserForm,RegisterForm1,RegisterForm2,setuserinfoForm
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


import hashlib
import random
import json
import datetime

# 这里是一个json的扩展用于格式化日期对象，如更新和新建数据日期
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

#read cache
def getcache(key):
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data

#write cache
def setcache(key, value):
    cache.set(key, json.dumps(value), settings.NEVER_REDIS_TIMEOUT)


# 登录
def login(request):
    if request.session.get('is_login', None):
        message = {'code': 2000, 'detail': '已经登录，不必重复进行！','userid':request.session.get('user_id')}
        return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
    if request.method == "POST" and "params" in json.loads(request.body):
        params=json.loads(request.body)['params']
        login_form = UserForm(params)
        message = {'code': 2001, 'detail': '请检查填写的内容！'}
        if login_form.is_valid():
            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(email=email)
                if user.password == password:  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['email'] = user.email
                    message = {'code': 2000, 'detail': '登录成功！','userid':user.id}
                else:
                    message = {'code': 2001, 'detail': '密码不正确！'}
            except:
                message = {'code': 2001, 'detail': '用户不存在！'}
        return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
 
    message = {'code': 2001, 'detail': '无requestMethod！'}
 
    return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")


# 注册接口1
def register1(request):
    if request.method == "POST" and "params" in json.loads(request.body):
        params=json.loads(request.body)['params']
        register_form = RegisterForm1(params)
        message = {'code': 2001, 'detail': '缺少必要参数！'}
        if register_form.is_valid():  # 获取数据
            email = register_form.cleaned_data['email']
            register2url = register_form.cleaned_data['register2url']
            same_email_user = models.User.objects.filter(email=email)
            if same_email_user:  # 邮箱地址唯一
                message = {'code': 2001, 'detail': '该邮箱地址已被注册，请使用别的邮箱！'}
                return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
            
            randnum = random.randint(0,9999)
            token = hash_code(str(randnum))
            # 设置email和令牌的缓存
            setcache(email,token)
            url=register2url+"?email="+email+"&token="+getcache(email)
            html_message = '<a href="'+url+'">进一步注册</a>'
            # 发邮件
            res = EmailMultiAlternatives('edu网站提醒您：',
                            '请点击下面的链接:' + html_message,
                            '1597591927@qq.com',
                            [email,])
            res.content_subtype = 'html'
            result = res.send()
            message = {'code': 2001, 'detail': result}
            
    return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

# 注册界面二
def register2(request):
    if request.method == "POST" and "params" in json.loads(request.body):
        params=json.loads(request.body)['params']
        register_form = RegisterForm2(params)
        message = {'code': 2001, 'detail': '缺少必要参数！'}
        if register_form.is_valid():  # 获取数据
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            token = register_form.cleaned_data['token']
            # 获取缓存中的令牌,进行对比
            if not getcache(email):
                message = {'code': 2001, 'detail': '该email暂无token，注册失败'}
                return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

            if not getcache(email)==token:
                message = {'code': 2001, 'detail': '该email和token不匹配'}
                return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")


            if not password1 == password2:  # 判断两次密码是否相同
                message = {'code': 2001, 'detail': '两次输入的密码不同！'}
                return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

            else:
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = {'code': 2001, 'detail': '该邮箱地址已被注册，请使用别的邮箱！'}
                    return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
                # 当一切都OK的情况下，创建新用户
                new_user = models.User.objects.create()
                
                # 本身是加密密码,和界面上的设置相孛,暂时去掉
                #new_user.password = hash_code(password1)  # 使用加密密码
            
                new_user.password = password1
                new_user.email = email
                new_user.save()
                message = {'code': 2000, 'detail': '注册成功！'}  # 自动跳转到登录页面
    return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
 
def logout(request):
    if not request.session.get('is_login',None):
        message = {'code': 2001, 'detail': '未登录！'}  # 未登录
    request.session.flush()
    message = {'code': 2000, 'detail': '注销成功！'}  # 自动跳转到登录页面
    return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")
 
def hash_code(s, salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

# 获取该用户的所有课程
def getallcourse(request):
    if request.method == "POST":
        uid=request.session.get('user_id',default=None)

        user = models.User.objects.filter(id=uid)
        courses = list(list(user)[0].course_set.all())

        courselist = []          ## 空列表
        # 返回标题和进行的百分比
        for course in courses:
            usercourses = UserCourse.objects.filter(user=list(user)[0],course=course).values()
            course=model_to_dict(course)
            usercourses=list(usercourses.values())
            course1 = {}
            course1['id'] = course['id']
            course1['title'] = course['title']
            course1['dopercent'] = usercourses[0]['dopercent']
            courselist.append(course1)

        message = {}
        message["courses"] = courselist

    return HttpResponse(json.dumps(message, ensure_ascii=False,cls=DateEncoder), content_type="application/json")

# 获取用户的信息
def getuserinfo(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not "userid" in json.loads(request.body)['params'] or json.loads(request.body)['params']['userid'] == '':
            message = {'code': 2001, 'detail': '缺少用户id！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

        params = json.loads(request.body)['params']
        user = models.User.objects.get(id=params['userid'])
        userdic = model_to_dict(user)
        if userdic['pic']:
            userdic['pic'] = settings.STATIC_URL_PRE + userdic['pic'].url
        else:
            userdic['pic'] = ""
        return HttpResponse(json.dumps(userdic, ensure_ascii=False), content_type="application/json")
# 设置用户信息
def setuserinfo(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not setuserinfoForm(json.loads(request.body)['params']).is_valid():
            message = {'code': 2001, 'detail': '缺少参数！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

        params = json.loads(request.body)['params']
        user = models.User.objects.get(id=params['userid'])
        # 本身可以设置图片但是界面上没有设置头像的地方,就注释掉了
        # user.pic = request.FILES.get('pic')
        if params['nickname']:
            user.nickname = params['nickname']
        # 本身是加密密码,和界面上的设置相孛,暂时去掉
        # user.password = hash_code(params['password'])
        user.password = params['password']
        if params['paypassword']:
            user.paypassword = params['paypassword']
        if params['telphone']:
            user.telphone = params['telphone']
        user.email = params['email']
        user.save()
        message = {'code': 2000, 'detail': '设置成功！'}
        return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")