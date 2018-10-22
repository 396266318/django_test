# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/10/22 14:50
"""
from django import forms


class AddProjectForm(forms.Form):
	name = forms.CharField(label="名称", max_length=100)
	describe = forms.Field(label="描述", widget=forms.Textarea)
	status = forms.BooleanField(label="状态")
