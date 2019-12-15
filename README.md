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
    