from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from polls.models import Poll
from polls.views import PollDetailView

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
    url(r'^(?P<pk>\d+)/$',
        PollDetailView.as_view()),
    url(r'^(?P<pk>\d+)/results/$', 
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)

