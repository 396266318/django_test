from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForm


@login_required
def project_manage(request):
	"""项目列表管理"""
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
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']
			Project.objects.create(name=name, describe=describe, status=status)
			return HttpResponseRedirect('/manage/project_manage/')
	else:
		form = ProjectForm()

	context = {
		"form": form,
		"type": "add",
	}
	return render(request, 'project_manage.html', context=context)


@login_required
def edit_project(request, pid):
	"""编辑项目"""
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			model = Project.objects.get(id=pid)
			model.name = form.cleaned_data['name']
			model.describe = form.cleaned_data['describe']
			model.status = form.cleaned_data['status']
			model.save()
			return HttpResponseRedirect('/manage/project_manage/')
	else:
		if pid:
			form = ProjectForm(instance=Project.objects.get(id=pid))
	context = {
		"form": form,
		"type": "edit",
	}
	return render(request, 'project_manage.html', context=context)


@login_required
def delete_project(request, pid):
	"""删除项目"""
	Project.objects.get(id=pid).delete()
	return HttpResponseRedirect("/manage/project_manage/")
