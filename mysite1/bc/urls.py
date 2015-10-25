from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.roll_list, name='roll_list'),
	url(r'^roll/(?P<pk>[0-9]+)/$', views.roll_detail, name='roll_detail'),
	url(r'^roll/new/$', views.roll_new, name='roll_new'),
]