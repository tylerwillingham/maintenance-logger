from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from cars import views

urlpatterns = [
    url(r'^vehicles/$', views.vehicle_list),  # vehicles/
]

urlpatterns = format_suffix_patterns(urlpatterns)