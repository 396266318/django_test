# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/9/30 16:52
"""
from django import forms
from django.forms import ModelForm
from project_app.models import Project, Module
from django.forms import fields


class AddProjectForm(forms.Form):
	"""Form项目表单"""
	name = forms.CharField(max_length=100)  # 名称
	describe = forms.CharField(max_length=300)  # 描述


class ProjectForm(ModelForm):
	"""项目表格"""
	class Meta:
		model = Project
		exclude = ['create_time']  # 在form 中不显示的字段


class ModuleForm(ModelForm):
	"""模块表格"""
	class Meta:
		model = Module
		exclude = ['create_time']  # Form 中不显示创建时间字段