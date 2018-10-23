# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/10/23 11:28
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Module
from project_app.forms import ModuleForm


@login_required
def module_manage(request):
	"""模块列表管理"""
	username = request.session.get('user1', '')
	module_all = Module.objects.all()
	context = {
		"user": username,
		"modules": module_all,
		"type": "list",
	}
	return render(request, "module_manage.html", context=context)


@login_required
def add_module(request):
	"""添加模块"""
	if request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			project = form.cleaned_data['project']
			Module.objects.create(
				name=name, describe=describe, project=project
			)
			return HttpResponseRedirect("/manage/module_manage/")
	else:
		form = ModuleForm()
	context = {
		"form": form,
		"type": "add",
	}
	return render(request, "module_manage.html", context=context)


@login_required
def edit_module(request, mid):
	"""编辑项目"""
	if request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			model = Module.objects.get(id=mid)
			model.name = form.cleaned_data['name']
			model.describe = form.cleaned_data['describe']
			model.project = form.cleaned_data['project']
			model.save()
			return HttpResponseRedirect("/manage/module_manage/")
	else:
		if mid:
			form = ModuleForm(instance=Module.objects.get(id=mid))
	context = {
		"form": form,
		"type": "edit",
	}
	return render(request, "module_manage.html", context=context)


@login_required
def delete_module(request, mid):
	"""删除模块"""
	Module.objects.get(id=mid).delete()
	return HttpResponseRedirect("/manage/module_manage/")