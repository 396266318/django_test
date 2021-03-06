# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/10/22 14:50
"""
from django import forms
from project_app.models import Project, Module


# class ProjectForm(forms.Form):
# 	name = forms.CharField(label="名称", max_length=100)
# 	describe = forms.Field(label="描述", widget=forms.Textarea)
# 	status = forms.BooleanField(label="状态")


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'describe', 'status']


class ModuleForm(forms.ModelForm):

	class Meta:
		model = Module
		exclude = ['create_time']