from django.conf.urls import url
from django.contrib.auth.views import login,logout
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),

    url(r'^post/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        #r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),

    url(r'^post/(?P<pk>\d+)/$',
        #r'(?P<post>[-\w]+)/$',
        views.post_detail2,
        name='post_detail2'),
    #url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^tagsearch/(?P<pk>\w+)/$', views.tag_search, name='tagSearch'),
    #url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search,name='searchBlog'),

    #url(r'^login/$', views.user_login, name='login'),

    url(r'^login/$', login,name='login'),
    url(r'^logout/$', logout,{'next_page': '/blog'},name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]