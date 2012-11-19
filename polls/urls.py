from django.conf.urls import patterns, include, url
# from polls import views

urlpatterns = patterns('polls.views',
  #ex:  /polls/
  url(r'^$', 'index'),
  #ex:  /polls/5/
  url(r'^(?P<poll_id>\d+)/$', 'detail'),
  #ex:  /polls/5/results/
  url(r'^(?P<poll_id>\d+)/results/$', 'results'),
  #ex:  /polls/5/vote/
  url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)