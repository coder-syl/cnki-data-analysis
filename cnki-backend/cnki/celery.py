from __future__ import absolute_import, unicode_literals  # 必须在最上面

import os
from celery import Celery
from django.conf import settings

# 配置环境变量
project_name = "cnki"
project_settings = '%s.settings' % project_name
print(project_name,project_settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

# 实例化 Celery
app = Celery(project_name,
             broker='redis://localhost:6379',
             backend='redis://localhost:6379'
             )
# 使用 Django 的 settings 文件配置 Celery
app.config_from_object('django.conf:settings')

# Celery 加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
