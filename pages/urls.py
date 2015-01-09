from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^(?P<name>[\w-]+)/$', views.page, name='page'),
)
