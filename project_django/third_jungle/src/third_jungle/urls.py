from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# from hello.views import hello
from polls.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'third_jungle.views.home', name='home'),
    # url(r'^third_jungle/', include('third_jungle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls')),
#     url(r'^hello/$', hello)
    url(r'^index/$', index)
)
