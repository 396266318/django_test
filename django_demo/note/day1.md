# 主流程  

* 安装 python 3.6 django==2.1
```
python 安装包
pip  python3.6自带
pip install pipenv 虚拟环境管理
创建目录 如 D:\ 盘
mkdir Code, 切换到 d:\Code
pwd 查看当前目录 D:\Code
pipenv --three  创建python 3 虚拟环境  --three 是python3
pipenv shell  进入到虚拟环境中
执行 pip install Django  安装最新的django 版本 也可以指定 Django 版本
安装指定版本  pip install Django==2.0

```

* 创建Django 项目

```
cmd 下 切换到 d:\Code 目录
pipenv shell  激活虚拟环境
django startproject django_demo
cd 切换到 django_demo 目录

```

* 创建APP
```
cd 切换到 test_platform 目录
python manage.py startapp user_app
```

* 配置django settings.py
```
APP 应用配置
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_app',  # 把创建的APP名称添加到这里来，每次创建APP都需要添加进来

templates 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 查找django项目下为 templates 的模板
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'zh-hans'  # 配置为中文

TIME_ZONE = 'Asia/Shanghai'  # 配置时区 中国/上海

# 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]  # 识别django 目录下static 静态文件目录

```
# Django 目录结构
* django_demo 父目录
* django-demo\django_demo  django配置目录
* django_demo  __init__.py  python 3 默认目录 认为当前目录是python 包
* django_demo settings.py   Django 配置文件
* django_demo urls.py       Django 项目的URL设置。可视其为你的django网站的目录 如: http:127.0.0.1/index
* django_demo wsgi.py       Django 服务器网关,暂时还没有用到

* Django App应用目录 user_app
* __init__.py  python3 默认目录 认为当前目录是python 包
* admin.py     后台管理页面
* apps.py      app模块配置
* models.py    主要用一个 Python 类来描述数据表。 称为模型(model) 。 运用这个类,你可以通过简单的 Python 的代码来创建、检索、更新、删除 数据库中的记录而无需写一条又一条的SQL语句
* tests.py     用于测试
* views.py     视图文件, 包含了页面的业务逻辑
* migrations   数据库相关目录

* manage.py  Django 一种命令行工具，允许你以多种方式与该Django项目进行交互

# 启动Django 服务
```
python manages.py runserver  启动django服务 默认为8000 端口
```

### django manage 命令
```
django-admin.exe startproject my_blog(项目名字)
python manage.py startapp article (APP名字)
python manage.py runserver  localhost  启动 Django 服务
python manage.py makemigrations  生成数据库迁移脚本
python manage.py migrate 执行 将迁移脚本映射到数据库中
python manage.py sqlmigrate blog  创建博客表字段
python manage.py createsuperuser  创建管理员密码
```

### Django MTV 模式
* M 代表模型(Model),即数据存取层。 该层处理与数据相关的所有事务： 如何存取、 如何验证有效
* T 代表模板(Template),即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。
* V 代表视图(View),即业务逻辑层。
* 在django_demo/urls 下面添加路由，在APP下面新建templates，存放html文件，views编写逻辑
