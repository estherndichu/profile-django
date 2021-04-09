from django.conf import settings
from django.conf.urls.static import static 
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.index,name='index'),
    url("^post/(\d+)", views.post, name="post"),
    url("^like/(\d+)", views.like, name="like"),
    url("^profile/(\d+)", views.profile, name="profile"),
    url("^userprofile/(\d+)", views.userprofile, name="userprofile"),
    url("^search/", views.search, name="search"),
    url('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    url('follow/<to_follow>', views.follow, name='follow')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)