# -*- coding: utf-8 -*-
"""
author: Xuan
time: 2018/11/6 3:45 PM
"""
from django.urls import path
from interface_app import views


urlpatterns = [
	# 用例管理
	path("case_manage/", views.case_manage),
	path("debug/", views.debug),
	path("api_debug/", views.api_debug),
]