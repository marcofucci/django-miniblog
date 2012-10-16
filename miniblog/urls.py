from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^blog/', include('blog.urls')),
    url(r'^$', redirect_to, {'url': 'blog/'}, name='homepage'),
)

urlpatterns += staticfiles_urlpatterns()
