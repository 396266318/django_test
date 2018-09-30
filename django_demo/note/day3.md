## 第三次课程
* 从 user_app/templates 移出 templates 到 django_demo下
* settings.py TEMPLATES 添加 templates 位置

```
TEMPLATES
'DIRS': [],
修改为:
'DIRS': [os.path.join(BASE_DIR, 'templates')],

```

* 添加 静态目录 static
```
在 setting 最后面添加
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
```
* 利用浏览器cookie 记录用户名，并显示在登录成功页面
```python
views.py
from django.contrib import auth  # 引入 auth 包
def login_action(request):
    if user is not None:
        auth.login(request, user)  # 记录用户登录状态
        request.session['user'] = username
        return HttpResponseRedirect("/project_manage/")
```

* 获取浏览器 cookis
```python
views.py
from django.contrib.auth.decorators import login_required

@login_required
def project_manage(request):
    username = request.session.get("user", '')  # 读取浏览器 session
    return render(request, "project_manage.html", {"user": username})
```

* 添加退出功能
```python
views.py
from django.contrib import auth
def logout(request):
    auth.logout(request)  # 清除用户登录状态
    response = HttpResponseRedirect('/')
    return response
```

* urls.py 添加 访问路径
```python
# 在 views.py 中添加了 project_manage, logout 函数
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('user_login/', views.login_action, name='user_login'),
    # path('accounts/login/', views.login_action, name='accounts_login'),
    path('project_manage/', views.project_manage, name='project_manage'),
    path('logout/', views.logout, name='logout'),
]
```