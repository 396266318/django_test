import json
import requests
from django_demo import common
from interface_app.models import TestTask
from project_app.models import Project, Module


"""
: 说明, 该文件中的接由前端JS调用, 返回JSON格式数据
"""

def save_task_data(request):
    """保存任务"""
    if request.method == "POST":
        name = request.POST.get("task_name", "")
        describe = request.POST.get("task_describe", "")
        cases = request.POST.get("task_cases", "")

        if name == "":
            return common.response_failed("任务的名称不能为空")

        task = TestTask.objects.create(name=name, describe=describe, cases=cases)

        if task is None:
            return common.response_failed("创建失败")
        
        return common.response_succeed(message="创建任务成功!")
    else:
        return common.response_failed("请求方法错误")