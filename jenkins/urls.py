from django.conf.urls import patterns, include, url
from .views import JenkinsHome, webhook

urlpatterns = patterns('',
    url(r'^$', JenkinsHome.as_view(), name="jenkins-home"),
    url(r'^webhook$', webhook, name='jenkins-webhook'),
)
