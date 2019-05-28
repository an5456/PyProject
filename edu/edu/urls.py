"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from user import views as loginview
from . import views as indexview
from course import views as courseview
from order import views as orderview
import xadmin
urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^xadmin', xadmin.site.urls),

    # 主页api param：无
    url(r'^index', indexview.index),

    #登录api  parm：username：邮箱，password：密码
    url(r'^user/login', loginview.login),

    #注册第一步api param：email：邮箱，register2url：注册二界面地址
    url(r'^user/register1', loginview.register1),

    #注册第二步api param:password1：设置密码 password2：再次输入设置密码 email：邮箱 token：第一次api发送邮件的令牌
    url(r'^user/register2', loginview.register2),

    #设置用户信息api param： userid 用户id nickname：昵称 password：密码 paypassword：付款密码 telphone：电话号 email：邮箱
    url(r'^user/setuserinfo', loginview.setuserinfo),

    #注销 param：无
    url(r'^user/logout', loginview.logout),

    #获取用户信息 param：userid：用户id
    url(r'^user/getuserinfo', loginview.getuserinfo),

    #获取用户全部课程 param： userid:用户id
    url(r'^user/getallcourse', loginview.getallcourse),

    #课程主页 param：id：课程id
    url(r'^course/index', courseview.index),

    #获取用户的course状态 param：courseid：课程id，userid：用户id
    url(r'^course/getusercourse', courseview.getusercourse),

    #课程目录列表：param：id：课程id
    url(r'^course/cataloglist', courseview.cataloglist),

    #课程视频目录列表 param：courseid：课程id userid:用户id
    url(r'^course/videolist', courseview.videolist),

    #更新任务状态： catalogid：目录id dotime：完成时间 userid：用户id
    url(r'^course/updatetask', courseview.updatetask),

    #用户和任务关系新建，已废弃，功能归于^course/updatetask接口
    url(r'^course/addtask', courseview.addtask),

    #播放界面所有信息  param：catalogid 目录id ,userid:用户id，courseid：课程id
    url(r'^course/play', courseview.play),

    #获取关于这个目录的所有信息，播放界面可用 param：catalogid目录id
    url(r'^course/getcatalog', courseview.getcatalog),

    #获取付款信息 param：id：课程id
    url(r'^course/getpayinfo', courseview.getpayinfo),

    #创建订单 param： userid 用户id courseid:课程id total_amount：消费总额 discount：折扣价格
    url(r'^order/addorder', orderview.addorder),

    #支付订单 param： orderid：订单id pay_method：付款方式：微信，支付宝，其他
    url(r'^order/payorder', orderview.payorder),
]
