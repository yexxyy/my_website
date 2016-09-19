
from  django.conf.urls import include,url
from . import views


urlpatterns = [

    url(r'^$',views.get_record_list),
    url(r'^(?P<id>\d+)/$',views.get_record_detail),
    url(r'^home$',views.get_record_list_view),
]

