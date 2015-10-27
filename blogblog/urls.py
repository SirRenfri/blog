from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
	#url(r'^newmessage$', views.new_message, name='new_message'),
]