#coding=utf8

from django.shortcuts import render
from django.template import loader
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


@login_required(login_url='/management/login/')
def index(request):
    return HttpResponse('欢迎来到管理界面')



def user_login(request):
    if request.method=='GET':
        print '哈哈哈'
        return render(request, 'management/login.html')




    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
    return HttpResponse('login page')
