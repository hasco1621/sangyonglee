from django.conf.urls import include, url, patterns

#from . import views

urlpatterns = [
    #url(r'^photos/', incoude(photos_urls)),

    url(r'^$', 'blog.views.index'),
    url(r'^(?P<uuid>[0-9a-f]{32})/$','blog.views.detail'), #{32} 32자리아니면 처리못함
    url(r'^(?P<pk>\d+)/$', 'blog.views.detail'),


]
