from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<plugin_name>[\w]+)$', views.get_plugin),
    url(r'^(?P<plugin_name>[\w]+)/(?P<checksum>[a-fA-F\d]{32})$', views.get_plugin)
]
