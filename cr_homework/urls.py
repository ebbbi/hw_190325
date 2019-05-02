
from django.conf.urls import url
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^new/$', views.new, name="new"),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^post/(?P<index>\d+)/$', views.post_detail, name="post_detail"), 
    url(r'^post/(?P<index>\d+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name="post_delete"), 
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)