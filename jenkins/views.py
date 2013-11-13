from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpResponse

# Create your views here.
class JenkinsHome(TemplateView):
    template_name = "jenkins/home.html"

def webhook(request):
    url = request.GET.get('url', None)
    return HttpResponse("successed! %s" % url)
