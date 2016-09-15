
from  django.conf.urls import include,url
from . import views


urlpatterns = [
    url(r'^records/',views.index),


]

