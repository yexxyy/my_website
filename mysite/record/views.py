from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

#records list
from django.views.decorators.http import require_GET


@require_GET
def index(request):

    #records=Record.objects.all().order_by('-date')
    return HttpResponse('records list')

