__author__ = 'root'

from django.http import HttpResponse

from django.shortcuts import render_to_response

from django.template.context_processors import csrf

from django.template import RequestContext

import models


def hello1(request):
        return render_to_response('static/page/login.html',{'a':100},
                              context_instance=RequestContext(request))


def abc(request):
        return render_to_response('static/page/abc.html',{'a':100},
                              context_instance=RequestContext(request))


def index(request):
        return render_to_response('static/page/index.html',{'a':100},
                              context_instance=RequestContext(request))

def login(request):

    if request.method == 'POST':
        if 'userName' in request.POST and 'password' in request.POST:
            if request.POST['userName'] == 'admin' and request.POST['password']=='admin':
                return render_to_response('static/page/index.html',{'a':100},
                                  context_instance=RequestContext(request))

    return render_to_response('static/page/home.html',{'a':100},
                              context_instance=RequestContext(request))

def show(request):
    user_list = models.userinfo.objects.all()
    return render_to_response('static/page/show.html' ,{'user_list':user_list} ,context_instance=RequestContext(request))

def show_user(request):
    user_list = models.userinfo.objects.all().values('user')
    return render_to_response('static/page/show.html' ,{'user_list':user_list} ,context_instance=RequestContext(request))

def show_id_user(request):
    user_list = models.userinfo.objects.all().values_list('id','user')
    return render_to_response('static/page/show.html' ,{'user_list':user_list} ,context_instance=RequestContext(request))

def get_id(request):
    user_list = models.userinfo.objects.get(id=1)
    return render_to_response('static/page/show.html' ,{'user_list':user_list} ,context_instance=RequestContext(request))

def get_user(request):
    user_list = models.userinfo.objects.get(user="yangfan")
    return render_to_response('static/page/show.html' ,{'user_list':user_list} ,context_instance=RequestContext(request))