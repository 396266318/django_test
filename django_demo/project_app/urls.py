# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/9/30 15:49
"""
from django.urls import path
from project_app import views


app_name = 'polls'

urlpatterns = [
	path('', views.project_manage),
	path('project/', views.project_manage),
	path('', views.add_project),
	path('module/', views.module_manage),
	path('add_module/', views.add_module),
	path('project_test/<int:id>/', views.project),
]
