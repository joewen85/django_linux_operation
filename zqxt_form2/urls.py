"""zqxt_form2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    url(r'^index/$', 'monitor.views.index'),
    url(r'^ajax_demo/$','monitor.views.ajax_demo'),
    url(r'^api/(?P<string>\S+)/(?P<string02>\S+)/(?P<string03>\S+)/$', 'webssh.views.api'),
    url(r'^logout/$', 'monitor.views.logout'),
    url(r'^login/$', 'monitor.views.login'),
    url(r'^register/$', 'monitor.views.register'),
    url(r'^cmdb/', 'cmdb.views.infor'),
    url(r'^server/', 'monitor.views.server'),
    url(r'^monitor/cpu/', 'monitor.views.cpu'),
    url(r'^monitorset/$', 'monitor.views.monitorset'),
    url(r'^show/', 'monitor.views.show'),
    url(r'^echart/', 'monitor.views.echart'),
    url(r'^testRelease/$', 'monitor.views.testRelease'),
    url(r'^formalRelease/$', 'monitor.views.formalRelease'),
    url(r'^servers/$', 'monitor.views.servers'),
    url(r'^filersync/$', 'monitor.views.filersync'),
    url(r'^program/$', 'monitor.views.program'),
    url(r'^servicemanage/$', 'monitor.views.servicemanage'),
    url(r'^linuxlog/$', 'monitor.views.linuxlog'),
    url(r'^servicelog/$', 'monitor.views.servicelog'),
    url(r'^deluser/$', 'monitor.views.deluser'),
    url(r'^questions/$', 'monitor.views.Questions'),
    url(r'^Experience/$', 'monitor.views.experience'),
    url(r'^monitort/$', 'monitor.views.monitort'),
    url(r'^webssh/$', 'monitor.views.websshtest'),
    #url(r'^monitor/showdisk/$', 'monitor.views.showdisk'),
    url(r'^monitor/memory/', 'monitor.views.memory'),
    url(r'^monitor/disk/', 'monitor.views.disk'),
    url(r'^admin/', include(admin.site.urls)),
    
]
