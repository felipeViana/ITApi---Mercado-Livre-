from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	#/polls/
	url(r'^$', views.index, name = 'index'),
	#/polls/5/
	url(r'^product/', views.detail, name = 'detail'),
	#/polls/5/results/
	url(r'^(?P<poll_id>\d+)/$', views.final, name = 'final'),

	url(r'^(?P<poll_id>\d+)/results/$', views.results, name = 'results'),
	#ex: /polls/5/vote/
	url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name = 'vote')
	)

