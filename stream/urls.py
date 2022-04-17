from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog_index', blog_index, name='blog_index'),
    path('blog_post', blog_post, name='blog_post'),
    path('news_index', news_index, name='news_index'),
    path('news_single', news_single, name='news_single'),
    path('speaking', speaking, name='speaking'),
    path('listening_single', listening_single, name='listening_single'),
    path('listening_video', listening_video, name='listening_video'),
    path('writing_index', writing_index, name='writing_index'),
    path('writing_newspost', writing_newspost, name='writing_newspost'),
    path('writing_post', writing_post, name='writing_post'),
    path('reading_index', reading_index, name='reading_index'),
    path('reading_detail', reading_detail, name='reading_detail'),
    path('reading_listing', reading_listing, name='reading_listing'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
