# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/9/30 16:52
"""
from django import forms
from django.forms import ModelForm
from project_app.models import Project, Module
from django.forms import fields


class ProjectForm(ModelForm):
	"""项目表单"""
	class Meta:
		model = Project
		exclude = ['create_time']  # 在form 中不显示的字段


class AddProjectForm(forms.Form):
	"""添加项目表单"""
	name = forms.CharField(max_length=100)
	describe = forms.CharField(max_length=300)


class AddModuleForm(forms.Form):
	"""添加模块表单"""
	project = fields.ChoiceField(
		choices=Project.objects.values_list('id', 'name')
	)

	def __init__(self, *args, **kwargs):
		super(AddModuleForm, self).__init__(*args, **kwargs)
		self.fields['project'].choices=Project.objects.values_list('id', 'name')
