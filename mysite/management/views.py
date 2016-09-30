#coding=utf8

from django.shortcuts import render
from django.template import loader
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse, HttpResponseForbidden
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import render, redirect

# Create your views here.


@login_required(login_url='/management/login/')
def index(request):
    return render(request, 'management/manage_page.html')


def user_login(request):
    if request.method=='GET':
        return render(request, 'management/login.html')
    else:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            #登录成功,向cookie中写入sessionid
            login(request,user)
            return redirect('/management')
        else:
            return redirect('/management/login')
        return HttpResponseNotFound("User does not exist")


@login_required(login_url='/management/login/')
def user_logout(request):
    logout(request)
    return redirect('/management/login')





