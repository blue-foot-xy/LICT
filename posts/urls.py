from django.urls import path
from django.views.generic import FormView
from django.urls import re_path

from posts.views import *
from .forms import PostForm


urlpatterns = [
    path('view-posts', Posts.as_view(), name='view-posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEdit.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
    path('view-domains', Domains.as_view(), name='view-domains'),
    path('domains/edit/<int:pk>/', DomainsEdit.as_view(), name='domains-edit'),
    path('domains/delete/<int:pk>/', DomainsDelete.as_view(), name='domains-delete'),
    path('view-news', NewsView.as_view(), name='view-news'),
    path('news/edit/<int:pk>/', NewsEdit.as_view(), name='news-edit'),
    path('news/delete/<int:pk>/', NewsDelete.as_view(), name='news-delete'),
    path('view-publications', Publications.as_view(), name='view-publications'),
    path('publications/edit/<int:pk>/', PublicationsEdit.as_view(), name='publications-edit'),
    path('publications/delete/<int:pk>/', PublicationsDelete.as_view(), name='publications-delete'),
    path('search/', Search.as_view(), name='search'),
]
