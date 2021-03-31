from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.index,name='index'),
    url("^post/(\d+)", views.post, name="post"),
    url("^like/(\d+)", views.like, name="like"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)