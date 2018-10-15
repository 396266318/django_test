from django.db import models

# Create your models here.


class Project(models.Model):
	"""项目表"""
	name = models.CharField("名称", max_length=50, blank=False, null=True)
	describe = models.TextField("描述", default=False)
	status = models.BooleanField("状态", default=True)
	create_time = models.DateTimeField("创建时间", auto_now=True)

	def __str__(self):
		return self.name

	# class Meta:
	# 	db_table = "project"
	
	
class Module(models.Model):
	"""模块表"""
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	name = models.CharField("名称", max_length=100, blank=False, default=False)
	describe = models.TextField("描述", default=False)
	create_time = models.DateTimeField("创建时间", auto_now=True)

	def __str__(self):
		return self.name

	# class Meta:
	# 	db_table = "module"