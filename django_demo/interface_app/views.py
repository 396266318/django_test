import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def case_manage(request):
	"""创建测试管理视图"""
	if request.method == "GET":
		return render(request, "case_manage.html", {"type": "list"})
	else:
		return HttpResponse("404")


def debug(request):
	"""创建/调试接口"""
	if request.method == "GET":
		return render(request, "api_debug.html", {"type": "debug"})
	else:
		return HttpResponse("404")


def api_debug(request):
	"""调试接口"""
	if request.method == "POST":
		url = request.POST.get("req_url")
		method = request.POST.get("req_method")
		parameter = request.POST.get("req_parameter")
		
		payload = json.loads(parameter.replace("'", "\""))
		
		if method == "get":
			r = requests.get(url, params=payload)
		
		if method == "post":
			r = requests.get(url, json=payload)
		
		return HttpResponse(r.text)
