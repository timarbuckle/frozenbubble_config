from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<device_id>[\w]+)$', views.appconfig),
]
