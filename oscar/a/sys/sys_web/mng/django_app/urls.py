from django.conf.urls.defaults import patterns, include, url
import a.sys.sys_web.server.authentication.views
import auth_conf
import django.conf

if django.conf.settings.A_ENABLE_DJANGO_ADMIN:
    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app1.views.home', name='home'),
    # url(r'^app1/', include('app1.foo.urls')),

    url(r'^m/client/login/$',      'a.sys.sys_web.server.authentication.views.login', {"env": auth_conf.env}),
    url(r'^m/client/api/export/$',      'a.sys.sys_web.mng.django_app.export_api.export'),
    url(r'^m/client/api/account/login/$',      'a.sys.sys_web.server.authentication.views.apiLogin', {"env": auth_conf.env}),
    url(r'^m/client/api/account/logout/$',     'a.sys.sys_web.server.authentication.views.apiLogout', {"env": auth_conf.env}),
    url(r'^m/client/api/account/session/$',    'a.sys.sys_web.server.authentication.views.apiSession', {"env": auth_conf.env}),

    url(r'^m/cyan/login/$',      'a.sys.sys_web.server.authentication.views.login', {"env": auth_conf.env}),
    url(r'^m/cyan/api/account/login/$',      'a.sys.sys_web.server.authentication.views.apiLogin', {"env": auth_conf.env}),
    url(r'^m/cyan/api/account/logout/$',     'a.sys.sys_web.server.authentication.views.apiLogout', {"env": auth_conf.env}),
    url(r'^m/cyan/api/account/session/$',    'a.sys.sys_web.server.authentication.views.apiSession', {"env": auth_conf.env}),

    url(r'^m/client/system/$',     'a.sys.sys_web.mng.django_app.system'),
    url(r'^m/client/api/system$',  'a.sys.sys_web.mng.django_app.apiSystem'),
    url(r'^m/cyan/system/$',     'a.sys.sys_web.mng.django_app.system'),
    url(r'^m/cyan/api/system$',  'a.sys.sys_web.mng.django_app.apiSystem'),

)

if django.conf.settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^m/try1/$',       'a.sys.sys_web.mng.django_app.try1'), 
        )

if django.conf.settings.A_ENABLE_DJANGO_ADMIN:
    urlpatterns += patterns('',
        # Uncomment the admin/doc line below to enable admin documentation:
        url(r'^m/admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        url(r'^m/admin/', include(admin.site.urls)),
        )


