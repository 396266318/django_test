# -*- coding: utf-8 -*-
"""
author: Xuan
time: 2018/11/4 10:02 PM
"""
from django.urls import path
from interface_app import views

urlpatterns = [
	# 项目管理
	path('case_manage/', views.case_manage),

]