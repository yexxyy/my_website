#-*- coding: utf-8 -*-
from PIL import Image
from django.http import HttpResponse
from django.views.decorators.http import require_GET
import  os
from django.conf import settings



def index(request):
	return HttpResponse("IF YOU SEE THIS SENTENCE, THE SERVER IS UP")


@require_GET
def get_pictures(request, file_path):
    path = os.path.join(settings.MEDIA_ROOT, file_path)
    img = Image.open(path)
    response = HttpResponse(content_type='image/jpeg')
    img.convert('RGB').save(response, 'jpeg')
    return response
