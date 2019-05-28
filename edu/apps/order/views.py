from django.shortcuts import render

from . import models
from user.models import User
from django.http import HttpResponse
from course.models import Course,UserCourse
from .forms import addorderForm,payorderForm
import json
import hashlib
import time

# Create your views here.

# 添加订单
def addorder(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not addorderForm(json.loads(request.body)['params']).is_valid():
            message = {'code': 2001, 'detail': '缺少参数！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

        params = json.loads(request.body)['params']

        if int(params['discount']) > int(params['total_amount']):
            message = {'code': 2001, 'detail': '折扣金额大于商品金额，不合法！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

        course = Course.objects.get(id=params['courseid'])
        user = User.objects.get(id=params['userid'])
        # 添加订单  用户 课程 订单id 状态 折扣 原价
        new_order = models.Order.objects.create(
            course = course,
            user = user,
            order_id = hash_code(time.time().__str__()),
            status = '待支付',
            discount = params['discount'],
            total_amount = params['total_amount']
        )
        new_order.save()

        message = {'code': 2000, 'detail': '创建订单成功，等待支付！'}
        return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

# 付款 
def payorder(request):
    if request.method == "POST":
        if not "params" in json.loads(request.body) or not payorderForm(json.loads(request.body)['params']).is_valid():
            message = {'code': 2001, 'detail': '缺少参数！'}
            return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

        params = json.loads(request.body)['params']
        order = models.Order.objects.get(id=params['orderid'])
        # 将这个用户加入该课程
        newuserobject = UserCourse.objects.create(user=order.user,course=order.course)
        newuserobject.save()
        # 更改订单状态为已支付
        order.pay_method = params['pay_method']
        order.status = '已支付'
        order.usercourse = newuserobject
        order.save()

        message = {'code': 2000, 'detail': '订单支付成功！'}
        return HttpResponse(json.dumps(message, ensure_ascii=False), content_type="application/json")

def hash_code(s, salt='mysite_order'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()