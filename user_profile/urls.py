''' defines url patterns for user_profile'''
from django.conf.urls import url,patterns,include
from django.contrib import admin
from . import views

from django.contrib.auth.views import login

urlpatterns = [
	# login page 
	url(r'^login/$',login, {'template_name': 'user_profile/login.html'}, 
		name='login'),
	# logout page 
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	# register page 
	url(r'^register/$', views.RegisterView.as_view(), name='register'),
]