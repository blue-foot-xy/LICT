from django.urls import path
from django.views.generic import FormView
from posts.views import *
from .forms import PostForm
from django.urls import re_path

urlpatterns = [
    path('view-posts', Posts.as_view(), name='view-posts'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEdit.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
]
