from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.views.generic.edit import UpdateView
from project_app.models import Project, Module
from project_app.forms import AddProjectForm, AddModuleForm, ProjectForm


@login_required
def project_manage(request):
	"""判断用户是否登录"""
	username = request.session.get('user', '')
	project_list = Project.objects.all()
	context = {
		"projects": project_list,
		"user": username,
		"type": "list",
	}
	return render(request, "project_manage.html", context=context)


@login_required
def add_project(request):
	"""添加项目"""
	username = request.session.get('user', '')

	if request.method == 'POST':
		form = AddProjectForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = 1
			Project.objects.create(name=name, describe=describe, status=status)
			return HttpResponseRedirect('/manage/project/')
	else:
		form = AddProjectForm()

	context = {
		"user": username,
		"form": form,
		"type": "add",
	}
	return render(request, 'project_manage.html', context=context)


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


def project(request, id=0):
	assert isinstance(request, HttpRequest)
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			if id:
				model = Project.objects.get(id=id)
			else:
				model = Project()
			model.name = form.cleaned_data['name']
			model.describe = form.cleaned_data['describe']
			model.status = form.cleaned_data['status']
			model.save()
		id = 0
		return HttpResponseRedirect("/manage/project/")
	else:
		if id:
			form = ProjectForm(
				instance=Project.objects.get(id=id)
			)
		else:
			form = ProjectForm()
	context = {
		"title": "变更记录",
		"form": form,
		"data": Project.objects.all(),
		"id": id,
		"type": "edit"
	}
	return render(request, "project_manage.html", context=context)
