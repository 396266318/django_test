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
from project_app.forms import AddProjectForm, ProjectForm
from django.views.generic.edit import UpdateView


@login_required
def project_manage(request):
	"""项目管理"""
	username = request.session.get('user', '')
	project_list = Project.objects.all()
	context = {
		"projects": project_list,
		"user": username,
		"type": "list"
	}
	return render(request, "project_manage.html", context=context)


@login_required
def add_project(request, pid):
	"""添加项目"""
	username = request.session.get('user', '')
	if request.method == 'POST':
		form = AddProjectForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = 1
			Project.objects.create(name=name, describe=describe, status=status)
			return HttpResponseRedirect("/manage/project")
	else:
		form = ProjectForm()
	context = {
		"user": username,
		"form": form,
		"type": 'add'
	}
	return render(request, 'project_manage.html', context=context)


@login_required
def edit_project(request, pid):
	"""编辑项目"""
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			if pid:
				model = Project.object.get(id=pid)
			else:
				model = Project()
			model.name = form.cleaned_data['name']
			model.describe = form.cleaned_data['describe']
			model.status = form.cleaned_data['status']
			model.save()
		return HttpResponseRedirect('/manage/project')
	else:
		if pid:
			form = ProjectForm(instance=Project.objects.get(id=pid))
		else:
			form = ProjectForm()
			
	context = {
		"title": "变更记录",
		"form": form,
		"data": Project.objects.all(),
		"id": pid,
		"type": "edit"
	}
	return render(request, 'project_manage.html', context=context)


@login_required
def delete_project(request, pid):
	"""删除项目"""
	Project.objects.get(id=pid).delete()
	return HttpResponseRedirect("/manage/project")