"""DjangoHack2017 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView


from django.conf import settings
from django.conf.urls.static import static

import re

def user(request):
#	return HttpResponse("User:"+str(request.META) + ":")
#	return HttpResponse("User:"+request.META["REMOTE_USER"] + ":")
	user = re.sub(r"[\w\d]+\\+", "", request.META["REMOTE_USER"])
	return HttpResponse(user)



urlpatterns = [
    url(r'^table/', include('table.urls')),
    url(r'^network/', include('network.urls')),
	url(r'^user$', user, name='user'),
	url(r'^alias$', user, name='user'),
	url(r'^user/$', TemplateView.as_view(template_name="user.html"), name='user'),
	url(r'^about$', TemplateView.as_view(template_name="about.html"), name='about'),
	url(r'^anomaly/$', TemplateView.as_view(template_name="anomaly.html"), name='anomaly'),
	url(r'^build-quality/$', TemplateView.as_view(template_name="build-quality.html"), name='build_quality'),
	url(r'^addin/$', TemplateView.as_view(template_name="addin.html"), name='addin'),
	url(r'^team/$', TemplateView.as_view(template_name="team.html"), name='team'),
	url(r'^extra/$', TemplateView.as_view(template_name="extra.html"), name='extra'),
	url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),

#    url(r'^admin/', admin.site.urls),
#	url(r'^user$', views.user, name='user'),
#    url(r'^$', home),
#    url(r'^$', 'DjangoHack2017.views.home', name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT) \
+ static(settings.CSS_URL, document_root=settings.CSS_ROOT) \
+ static(settings.JS_URL, document_root=settings.JS_ROOT)
