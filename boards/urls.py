from boards import views
from boards.views import homepage, discuss
from django.conf.urls import url

urlpatterns = [
    url(r'^$', homepage),
    url(r'^discuss/$', discuss),
    url(r'^discuss/boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
]
