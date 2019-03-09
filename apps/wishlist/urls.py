from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^add_item$', views.add_item, name="add_item"),
    url(r'^submit_item$', views.submit_item, name="submit_item"),
    url(r'^join/(?P<item_id>\d+)$', views.join, name="join"),
    url(r'^unjoin/(?P<item_id>\d+)$', views.unjoin, name="unjoin"),
    url(r'^delete/(?P<item_id>\d+)$', views.delete, name="delete"),
    url(r'^show/(?P<item_id>\d+)$', views.show, name="show"),
    url(r'^profile/(?P<item_user_id>\d+)$', views.profile, name="profile")
]