from django.conf.urls import *
from . import views


app_name = 'messaging'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user_detail'),
    url(r'^(?P<user_id>[0-9]+)/conversation/$', views.convo, name='convo_view'),
    url(r'^$', views.UserIndexView.as_view(), name='results')
]