from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[\w\d]+)/(?P<id>[\w\d\-_\.]+)/$', views.my_network, name='my_network')
]
