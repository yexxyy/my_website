
from  django.conf.urls import include,url
from . import views


urlpatterns = [
    url(r'^$',views.get_record_list_view),
    url(r'^(?P<record_type>\w*)\/*$',views.get_record_list),
    url(r'^(?P<id>\d+)/$',views.get_record_detail),

]

