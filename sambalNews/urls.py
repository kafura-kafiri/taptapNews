from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^create_news$', views.create_news, name='create_news'),
    url(r'^add_comment/(?P<news_id>\w{0,50})$', views.add_comment),
    url(r'^next$', views.next, name='next'),
    url(r'^add_hashtag$', views.add_hashtag, name='add_hashtag'),
    url(r'^comments/(?P<news_id>\w{0,50})$', views.comments, name='comments'),
    url(r'^block/(?P<username>^\w+$)$', views.block, name='block'),
    url(r'^img/(?P<news_id>\w{0,50})$', views.img, name='img'),
]