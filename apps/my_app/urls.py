from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<number>\d+)$', views.destroy),   
    url(r'^remove/(?P<number>\d+)$', views.remove)     # This line has changed!
]