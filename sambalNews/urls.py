from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^create_news$', views.create_news, name='create_news'),
    url(r'^add_comment/(?P<news_id>\w{0,50})$', views.add_comment, name='add_comment'),
    url(r'^next$', views.next, name='next'),
    url(r'^add_hashtag$', views.add_hashtag, name='add_hashtag'),
    url(r'^comments/(?P<news_id>\w{0,50})$', views.comments, name='comments'),
    url(r'^get_news/(?P<news_id>\w{0,50})$', views.get_news, name='get_news'),
    url(r'^delete_news/(?P<news_id>\w{0,50})$', views.delete_news, name='delete_news'),
    url(r'^block/(?P<blocked_username>\w{0,50})$', views.block, name='block'),
    url(r'^img/(?P<news_id>\w{0,50})$', views.img, name='img'),
    url(r'^validate/(?P<news_id>\w{0,50})$', views.validate, name='validate'),
    url(r'^upgrade_user/(?P<code>\w{0,50})$', views.upgrade_user, name='upgrade_user'),
]