from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^thanks$', views.ThanksView.as_view(), name='thanks'),
    # ex: /polls/5/
    #url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]