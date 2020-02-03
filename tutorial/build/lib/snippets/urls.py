from django.conf.urls import url
#from rest_framework.urlpatterns import format_suffix_patterns #这个有bug！去掉，_frozen_importlib._DeadlockError: deadlock detected by _ModuleLock('django.test.signals') at
from snippets import views
from snippets.myviews import index
urlpatterns = [
    url(r'^api/snippets/$', views.SnippetList.as_view()),
    url(r'^api/snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^html/snippets/(?P<pk>[0-9]+)/$',index.get_snippet),
    url(r'^html/snippets/$',index.get_snippets)
]

#urlpatterns = format_suffix_patterns(urlpatterns)