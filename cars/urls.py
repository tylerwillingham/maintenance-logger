from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from cars import views

urlpatterns = [
    url(r'^vehicles/(?P<username>\w{0,50})$', views.vehicle_list),  # vehicles/
]

urlpatterns = format_suffix_patterns(urlpatterns)