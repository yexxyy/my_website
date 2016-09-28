#coding=utf8

from django.shortcuts import render
from django.template import loader
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse, HttpResponseForbidden
from django.views.decorators.http import require_GET, require_POST
# Create your views here.


@login_required(login_url='/management/login/')
def index(request):
    return HttpResponse('欢迎来到管理界面')



def user_login(request):
    if request.method=='GET':
        return render(request, 'management/login.html')
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        print username
        user=authenticate(username=username,password=password)

        if user is not None:
            return render(request,'management/manage_page.html')
        else:
            return HttpResponseBadRequest('Login fail')

        return HttpResponseNotFound("User does not exist")
