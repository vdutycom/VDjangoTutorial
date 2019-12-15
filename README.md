=====
VDjangoTutorial，职道®出品
=====

VDjangoTutorial 是一个Django和django REST API framework 学习样例软件，可以自由下载学习使用。

其中包括django项目的打包方法，uwsgi的运行配置，uwsgi+nginx的配置，打包setup.py的配置，和gunicorn的运行方法；
本项目开发环境为：python3.8，django3.0，开发工具：visual studio code

Quick start
-----------

1.现安装好您的python环境；并创建虚拟环境env； 


2. 克隆本项目分支publishMehod，然后可用vscode打开；

3. 打包：

4. gunicorn启动项目 

 gunicorn tutorial.wsgi:application -b 127.0.0.1:58005 
 多进程：
 gunicorn tutorial.wsgi:application -w 8 -k gthread -b 127.0.0.1:58005;


6. uwsgi的nginx配置：

uwsgi启动：
uwsgi –ini tutorial_uwsgi.ini

#django app

upstream tutorial {

        server 127.0.0.1:58005;

    }

server {

        server_name 127.0.0.1 localhost 192.168.50.95;

        listen      80;

        charset     utf-8;

        # max upload size

        client_max_body_size 75M;

        location /static {

            alias  /Users/yeluxing/Desktop/mydevelop/python/study/tutorial2/tutorial/webstatic/;

        }

        location / {

             include /usr/local/etc/nginx/uwsgi_params;

             uwsgi_pass tutorial;

             #uwsgi_pass  127.0.0.1:58005; #一定要和wsgi的.ini配置文件里的socket配置一样

        }

   }
7. 关于django的mysql链接错误解决：
用uwsgi启动项目后，出现错误Error loading MySQLdb module.
然后 pip install MySQL-python

又出现错误：

ModuleNotFoundError: No module named ‘ConfigParser’ 原因是MySQL-python不支持python3

解决
安装pymql：
pip install pymysql
django项目__inti__.py中添加以下代码
import pymysql
pymysql.install_as_MySQLdb()
又会报错：设置uwsgi配置文件的home，home的路径为虚拟环境的路径，如下

[uwsgi]

home = /Users/yeluxing/Desktop/mydevelop/python/study/tutorial/env

http = 0.0.0.0:8005 #ng里用proxy_pass

socket=0.0.0.0:58005 #这个才是重点，ng里用uwsgi_pass

module = tutorial.wsgi

#项目的路径

chdir = /Users/yeluxing/Desktop/mydevelop/python/study/tutorial2/tutorial

wsgi-file = tutorial/wsgi.py

processes = 4

static-map = /static= /Users/yeluxing/Desktop/mydevelop/python/study/tutorial2/tutorial/webstatic

stats = 127.0.0.1:9191

启动又报错：

django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.
https://www.cnblogs.com/dotnetcrazy/p/10779304.html

就是更改django里的mysql 的base文件注解掉

/Users/yeluxing/Desktop/mydevelop/python/study/tutorial/env/lib/python3.8/site-packages/django/db/backends/mysql/base.py

if version < (1, 3, 13):

    #raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

    pass    