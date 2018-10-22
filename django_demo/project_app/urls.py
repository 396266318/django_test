# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/9/30 15:49
"""
from django.urls import path
from project_app import views


urlpatterns = [
	path('project_manage/', views.project_manage),
	path('add_project/', views.add_project),
	path('edit_project/', views.edit_project),
]
