from django.conf.urls import url

from . import views
from .views import IndexView,DetailView,ResultsView
from django.contrib.auth.decorators import login_required

app_name = 'polls'
urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]