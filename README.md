# 这是一个可重用的登录和注册APP

#简单的使用方法：

创建虚拟环境
使用pip安装第三方依赖
修改settings.example.py文件为settings.py
运行migrate命令，创建数据库和数据表
运行python manage.py runserver启动服务器

路由设置

from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'index/',views.index),
    path(r'login/',views.login),
    path(r'register/',views.register),
    path(r'logout/',views.logout),
    path(r'captcha/',include('captcha.urls')),
    path('confirm/', views.user_confirm),
]