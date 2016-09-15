#-*- coding: utf-8 -*-
from PIL import Image
from django.http import HttpResponse
from django.views.decorators.http import require_GET
import  os

from image.templatetags import img


def index(request):
	return HttpResponse("IF YOU SEE THIS SENTENCE, THE SERVER IS UP")



@require_GET
def get_pictures(request, file_path):

    print 'request'+request
    print 'file_path'+file_path


    path = os.path.join('/Users/yetongxue/Desktop/my_website/uploads', file_path)
    response = HttpResponse(mimetype="image/gif")
    img = Image.open(path)
    img.save(response,'jpg')



    return response
