from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<query>SELECT.+)$', views.select, name='select'),
#    url(r'^MyNetwork/(?P<name>[\w\d]+)/(?P<id>[\w\d\-_\.]+)/$', views.my_network, name='my_network'),
#    url(r'^MyNetwork/(?P<name>[\w\d]+)/(?P<id>[\w\d\-_\.]+)/$', network.get_influence_score, name='get_influence_score'),
    url(r'^(?P<name>[\w\d]+)/$', views.table, name='table'),
    url(r'^(?P<name>[\w\d]+)/(?P<column>[\w\d_]+)/(?P<value>[\w\d\-_\.]+)/$', views.table, name='table'),
]
