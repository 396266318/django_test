# -*- coding: utf-8 -*-
"""
author: Xuan
time: 2018/11/6 3:45 PM
"""
from django.urls import path
from interface_app.views import testcase_views


urlpatterns = [
	# 用例管理
	path("case_manage/", testcase_views.case_manage),
	path("add_case/", testcase_views.add_case),
	path("api_debug/", testcase_views.api_debug),
	path("save_case/", testcase_views.save_case),
	path("get_project_list/", testcase_views.get_project_list),
	path("search_case_name/", testcase_views.search_case_name),
	path("debug_case/<int:cid>/", testcase_views.debug_case),
	path("get_case_info/", testcase_views. get_case_info)
]