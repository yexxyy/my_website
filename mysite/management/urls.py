#coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name='index'),

    #登录登出
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),

    #获取记录列表/删除记录
    url(r'^record/(?P<type_or_id>\w*)\/*',views.get_records,name='get_records'),

]