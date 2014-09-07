from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static
from dj import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dj.views.hello', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
