from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect

from .models import *
from .forms import *


class Posts(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        posts = Post.objects.all().order_by('-publish_date')
        context = {
            'form': form,
            'posts': posts
        }

        return render(request, 'posts/view_posts.html', context)

    def post(self, request, *args, **kwargs):
        if 'save_button' in request.POST:
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.publisher = request.user
                new_post.save()
                form = PostForm() # Clearing the form after submission

            # TODO: REDIRECT TO POST'S DETAIL PAGE INSTEAD
            return redirect('view-posts')
        else:
            #TODO: upload file and pass the url
            pass



class PostDetail(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        context = {
            'post': post,
        }

        return render(request, 'posts/post_detail.html', context)


class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','body']
    template_name = 'posts/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('view-posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher
