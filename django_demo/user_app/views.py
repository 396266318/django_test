from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index(request):
	"""首页"""
	return render(request, 'index.html')


def login_action(request):
	"""处理登录请求"""
	if request.method == "POST":
		username = request.POST.get("username", "")
		password = request.POST.get("password", "")
		if username == "" or password == "":
			return render(request, 'index.html', {"error": "用户名或者密码错误"})

		else:
			user = auth.authenticate(username=username, password=password)  # 验证用户是不是存在

			if user is not None:
				auth.login(request, user)  # 记录用户登录状态
				request.session['user'] = username
				return HttpResponseRedirect("/manage/project_manage/")
		login_username = request.POST.get("username")
		login_password = request.POST.get("password")
		if login_username == "" or login_password == "":
			return render(request, 'index.html', {"error": "用户名或者密码错误"})

		else:
			user = auth.authenticate(username=login_username, password=login_password)

			if user is not None:
				auth.login(request, user)  # 记录用户登录状态
				response =  HttpResponseRedirect("/manage/project/")
				request.session['user'] = login_username
				return response
			else:
				return render(request, 'index.html', {"error": "用户名或者密码错误"})
	else:
		return render(request, 'index.html')

# @login_required
# def project_manage(request):
# 	"""获取浏览器session"""
# 	username = request.session.get("user", '')  # 读取浏览器 session
#
	# return render(request, "project_manage.html", {"user": username})


def logout(request):
	"""登录退出"""
	auth.logout(request)  # 清除用户登录状态
	response = HttpResponseRedirect('/')
	return response


# @login_required
# def add_project(request):
# 	"""添加项目"""
# 	if request.method == "POST":
# 		form = ProjectForm(request.POST)
# 		if form.is_valid():
# 			return HttpResponseRedirect('/thanks/')
# 	else:
# 		form = ProjectForm()
# 	return render(request, 'project_manage.html', {"form": form})
