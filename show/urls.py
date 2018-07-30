from django.conf.urls import url
from . import views

'''
路由
'''

urlpatterns = [

    url(r'^$', views.index, name='show_index'),
    # url(r'detail', views.detail, name='detail'),
    url(r'^(?P<idint>\d+)/detail_id/$', views.detail_id, name='detail_id'),
    url(r'^(?P<city_str>[a-zA-Z\u4e00-\u9fa5]+)/detail_city/$', views.detail_city, name='detail_city'),
    url(r'^(?P<povins_str>[a-zA-Z\u4e00-\u9fa5]+)/detail_povins/$', views.detail_povins, name='detail_povins'),
    url(r'^(?P<region_str>[a-zA-Z\u4e00-\u9fa5]+)/detail_regin/$', views.detail_regin, name='detail_regin'),
    url(r'^hole_list/', views.hole_list, name='hole_list'),
    url(r'^by_city/', views.by_city, name='by_city'),
    url(r'^by_province/', views.by_province, name='by_province')

]

# url(r'^detail/?P<id>(\\d+)', views.detail_id, name='detail_id'),
# url(r'^(?P<name>[a-z]+)/(?P<age>\d{1,3})/(?P<gender>["男"|"女"])/index1/$', views.index1, name="index1"),
