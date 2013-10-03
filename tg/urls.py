from django.conf.urls import patterns, include, url
from qa.views import qa
from orders.views import to_order, thx
from contacts.views import contacts

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    # (r'^ckeditor/', include('ckeditor.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^tinymce/', include('tinymce.urls')),

    url(r'^$', include('news.urls')),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^catalog/(\d+)/', to_order),
    url(r'^thx/', thx),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/$', contacts),
    url(r'^qa/', qa),
)
