### conda配置清华镜像

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

## pip 　配置清华镜像

windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，新建文件pip.ini，内容如下

```ini
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 安装所需插件

####  自动

```python
pip install -r requirements.txt
```

#### 手动

```python
pip install celery
pip install django-celery
pip install django
pip install pymysql
pip install redis==2.10.6
pip install celery-with-redis
pip install selenium

```

### 配置MySQL数据库

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'cnki',         # 你要存储数据的库名，事先要创建之
        'USER': 'root',         # 数据库用户名
        'PASSWORD': 'root',     # 密码
        'HOST': 'localhost',    # 主机
        'PORT': '3306',         # 数据库使用的端口
    }
}
```

### 生成表结构

```python
python manage.py makemigrations
python manage.py migrate
```



### 安装配置redis

cnki/settings.py

```python
BROKER_URL = 'redis://127.0.0.1:6379/1'
```



### 启动程序

#### 启动celery服务

```
celery -A cnki worker -l info
```

#### 启动django

```
python manage.py runserver
```

#### 访问

http://127.0.0.1:8000/cnki/

### Django使用channels实现websocket并解决报错object.__init__() takes no parameters