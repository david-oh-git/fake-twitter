
''' defines url patterns for tweets '''
from django.conf.urls import url,patterns,include
from django.contrib import admin
from . import views
admin.autodiscover()


urlpatterns = [
	# Home page
	url(r'^$',views.Index.as_view(), name='index'),
]


