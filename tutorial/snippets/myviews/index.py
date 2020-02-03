from django.http import HttpResponse
from snippets.models import Snippet
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import   permission_required,login_required

'''
permission_required权限判断
'snippets.add_snippet' , 'snippets' 为appname,'add_snippet'为数据库的表的codename字段的名称，意为添加snippet。
可以通过添加关系表‘auth_user_user_permissions’的user_id和permission_id来添加用户的权限
'''
@permission_required('snippets.add_snippet',"/admin/login")
def get_snippet(request,pk):
    user = request.user #获取当前的用户
    print("current user's permissions:", user.get_all_permissions())#获取当前用户的权限列表
    #if request.user.has_perm('aptest.add_hv'): #检查用户是否具有add权限，如果没有则不能保存新增内容
    if pk:
        snippet = Snippet.objects.get(id=pk)
   
    context = {
        
        'title':'view 测试',
        'snippet':snippet
    }
    print("-------------snipet:",pk,snippet.code)  
    return render(request,'snippets/snippet.html',context=context)  

@login_required(login_url="/admin/login")
def get_snippets(request):
    user = request.user #获取当前的用户
    print("user name",user)
    if user.has_perm('snippets.view_snippet'):#检查用户是否具有view_snippet权限，如果没有则不能保存新增内容
        snippets = Snippet.objects.all()
        context = {
            'isPermission':True,
            'title':'view 测试',
            'snippets':snippets
        }
        print("-------------snipets:",snippets[0].code) 
    else :
        context = {
            'title':'view 测试--没有权限',
            'isPermission':False,
            
        }       
    return render(request,'snippets/snippets.html',context=context)    


