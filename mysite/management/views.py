#coding=utf8


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
import types
from .models import Record



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



@login_required(login_url='/management/login/')
def get_records(request,type_or_id):


    records=Record.objects.all().order_by('-date')
    json_list=[]
    if type_or_id=='': #请求所有列表
        pass

    if type(type_or_id)==types.UnicodeType: #请求指定类型列表
        records.filter(Record.record_type==type_or_id)
        print 'type_list'
    if type(type_or_id) is types.IntType: #请求指定id 记录
        records.filter(Record.id==type_or_id)
        print 'id_'


    for record in records:
        record_detail = record.to_json()
        json_list.append(record_detail)

    return JsonResponse({
        'status':200,
        'message':'获取记录成功',
        'list':json_list,
    })