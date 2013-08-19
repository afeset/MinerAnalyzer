from django.conf.urls.defaults import patterns, include, url
import auth_conf

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tech.views.home', name='home'),
    # url(r'^tech/', include('tech.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^tech/logout/$',              'a.sys.sys_web.server.authentication.views.apiLogout', {"env": auth_conf.env}),
    url(r'^tech/content/(?P<path>.*)$', 'a.sys.sys_web.tech.content_portal.serveContent'),
    url(r'^tech/streamVideo/(?P<path>.*)$', 'a.sys.sys_web.tech.content_portal.streamVideo'),
)
