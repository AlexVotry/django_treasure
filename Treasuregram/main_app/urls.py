from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/doc/', include('admin.contrib.admindocs.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, }),
    ]
