from django.conf.urls import patterns, url

from ipts import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
		url(r'^(?P<pk>\d+)/results/$', views.results, name='results'),
		url(r'^(?P<pk>\d+)/chosen/$', views.chosen, name='chosen'),
		url(r'^resultsAll/$', views.resultsAll, name='resultsAll'),
)
