from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^roll/list/$', views.roll_list, name='roll_list'),
	url(r'^roll/(?P<pk>[0-9]+)/$', views.roll_detail, name='roll_detail'),
	url(r'^$', views.roll_new, name='roll_new'),
	url(r'^accounts/logout/$', views.logout_view, name='logout_view'),
	url(r'^roll/(?P<pk>[0-9]+)/edit/$', views.roll_edit, name='roll_edit'),
]
