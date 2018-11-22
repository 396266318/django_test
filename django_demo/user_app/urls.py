# -*- coding: utf-8 -*-
"""
author: xuan
time: 2018/10/15 15:27
"""
# from django.conf.urls import url, include
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'is_staff')
		

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializers_class = UserSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]