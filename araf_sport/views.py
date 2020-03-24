from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


def index(request):
    context = {'title': 'Araf Sport'}
    return render(request, 'araf_sport/index.html', context)


def logout(request):
    context = {'title': 'Araf Sport'}
    return HttpResponseRedirect('araf_sport/index.html',context)


def pics(request):
    context = {'title': 'Pics Page'}
    return render(request,'araf_sport/pics.html',context)


def workouts(request):
    context = {'title': 'Workout Plans'}
    return render(request,"araf_sport/workouts.html",context)
