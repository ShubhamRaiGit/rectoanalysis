from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^facebook/$', views.facebook, name='facebook_page'),
    url(r'^twitter/$', views.twitter, name='twitter_page'),
    url(r'^twitter/(?P<tracking_num>[\w-]+)/$', views.tracker_view, name="tracker_details")
]