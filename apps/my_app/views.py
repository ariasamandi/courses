# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        "Course" : Course.objects.all()
    }
    return render(request, 'my_app/index.html', context)
def add(request):
    Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
    return redirect('/')
def remove(request, number):
    Course.objects.get(id=number).delete()
    return redirect('/')
def destroy(request, number):
    context = {
        "Course" : Course.objects.get(id=number)
    }
    return render(request, 'my_app/destroy.html', context)