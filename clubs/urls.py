from django.conf.urls import url
from clubs import views

urlpatterns = [
    url(r'^clubs/$', views.club_list),
    url(r'^notices/$', views.notices_list),
#    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]
