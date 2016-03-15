
from django.conf.urls import url
from . import views

urlpatterns = [

#   URL for Home Page

    url(r'^$' , views.post_list , name='post_list'),


#   URL for A Post's Page

    url(r'^post/(?P<post_id>\d+)/$' , views.post_page, name = 'post_page' ),


#   URL for Adding a New Post

#    url(r'^post/new/$' , views.add_post , name='add_post'),

#   {%		url 'add_post'    %}
]
