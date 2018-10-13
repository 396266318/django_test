# -*- coding: utf-8 -*-
"""
author: Xuan
time: 2018/10/13 8:10 PM
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from project_app.models import Project, Module
from django.forms.models import model_to_dict
from project_app.forms import ProjectForm, ModuleForm
from django.views.generic.edit import UpdateView


@login_required
def module_manage(request):
	"""模块管理"""
	username = request.session.get('user', '')
	modules = Module.objects.all()
	module_list = []
	for module_ in modules:
		module_dict = model_to_dict(module_)
		module_dict['create_time'] = module_.create_time
		project_obj = Project.objects.get(pk=module_dict["project"])
		module_dict["project"] = project_obj.name
		module_list.append(module_dict)
	context = {
			"modules": module_list,
			"user": username,
			"type": "list",
		}
	return render(request, "module_manage.html", context=context)


def add_module(request):
	"""添加模块"""
	username = request.session.get('user', '')
	if request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			project_name = form.cleaned_data['project']
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			project_obj = Project.objects.get(name=project_name)
			Module.onjects.create(name=name, describe=describe, project_id=int(project_obj.id))
			return HttpResponseRedirect('/manage/module/')
	else:
		form = ModuleForm()
	context = {
		"user": username,
		"form": form,
		"type": "add"
	}
	return render(request, 'module_manage.html', context=context)


@login_required
def edit_module(request, mid):
	"""编辑模块"""
	if request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			if mid:
				model = Module.object.get(id=mid)
			else:
				model = Module()
			model.name = form.cleaned_data['name']
			model.describe = form.cleaned_data['describe']
			model.project = form.cleaned_data['project']
			model.sava()
			return HttpResponseRedirect('/manage/module/')
		else:
			if mid:
				form = ModuleForm(
					instance=Module.objects.get(id=mid)
				)
			else:
				form = ModuleForm()
			context = {
				'title': "变更记录",
				'form': form,
				'data': mid,
				'type': 'edit'
			}
			return render(request, 'module_manage.html', context=context)


@login_required
def delete_module(request, mid):
	"""删除模块"""
	Module.objects.get(id=mid).delete()
	return HttpResponseRedirect("/manage/module")