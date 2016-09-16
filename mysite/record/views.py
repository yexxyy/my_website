#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Record
from django.http import Http404


#records list
from django.views.decorators.http import require_GET

@require_GET
def index(request):
    records=Record.objects.all().order_by('-date')
    json_list=[]
    for record in records:
        record_detail=record.to_json()
        json_list.append(record_detail)

    return JsonResponse({
        'status':200,
        'message':'获取记录列表成功',
        'list':json_list,
    })

@require_GET
def detail(request,id):
    try:
        record=Record.objects.get(pk=id)
    except Record.DoesNotExist:
        raise Http404('记录不存在')

    return JsonResponse(record.to_json())


