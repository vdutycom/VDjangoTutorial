from tutorial.form import LoginForm
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views import View

class Index(View):
    def get(self,request):
        if request.user.is_authenticated:
            user = request.user
            print('user is logined!')
            return render(request,"index.html",{"user":user})
        else:
            print("user is not logined")
            return render(request,"index.html",{"user":"未登录"})


class LoginView(View):

    def get(self, request):
        # if not request.user.is_authenticated:
        login_form = LoginForm(request.GET)
        return render(request, 'registration/login.html',{"forms":login_form})
        # else:
        #     return HttpResponseRedirect('/')

    def post(self, request):
        redirect_to = request.GET.get('next', '/')
        login_form = LoginForm(request.POST)
        ret = dict(login_form=login_form)
        ret["resultCode"] = 0
        if login_form.is_valid():
            user_name = request.POST['username']
            pass_word = request.POST['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(redirect_to)
                else:
                    ret['msg'] = '用户未激活！'
            else:
                ret['msg'] = '用户名或密码错误！'
        else:
            ret['msg'] = '用户和密码不能为空！'
        return render(request, 'registration/login.html', ret)

class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))#reverse通过名称，反向获取url