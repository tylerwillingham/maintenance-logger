from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maintenance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # rest framework browsable api
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Apps:
    url(r'', include('cars.urls')),  # cars
    url(r'', include('maintenance_history.urls')),  # maintenance
)
