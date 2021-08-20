from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect

from user.models import UserProfile
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
        posting_permission = UserProfile.objects.get(pk=request.user.pk).posting_permission
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if posting_permission:
                new_post = form.save(commit=False)
                new_post.publisher = request.user
                new_post.save()
                form = PostForm() # Clearing the form after submission
            else:
                return render(request, 'posts/no_permission.html')
        return redirect('view-posts')


class PostDetail(View):
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


class Domains(View):
    def get(self, request, *args, **kwargs):
        form = ResearchDomainForm
        posts = ResearchDomains.objects.all().order_by('-publish_date')
        context = {
            'form': form,
            'posts': posts
        }

        return render(request, 'posts/view_domains.html', context)

    def post(self, request, *args, **kwargs):
        posting_permission = UserProfile.objects.get(pk=request.user.pk).posting_permission
        form = ResearchDomainForm(request.POST, request.FILES)
        if form.is_valid():
            if posting_permission:
                new_post = form.save(commit=False)
                new_post.publisher = request.user
                new_post.save()
                form = ResearchDomainForm() # Clearing the form after submission
            else:
                return render(request, 'posts/no_permission.html')

        return redirect('view-domains')


class DomainsEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ResearchDomains
    fields = ['title','body']
    template_name = 'posts/domains_edit.html'

    def get_success_url(self):
        return reverse_lazy('view-domains')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class DomainsDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ResearchDomains
    template_name = 'posts/domains_delete.html'
    success_url = reverse_lazy('view-domains')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher



class Publications(View):
    def get(self, request, *args, **kwargs):
        form = ResearchPublicationForm
        posts = ResearchPublicationList.objects.all().order_by('-publish_date')
        context = {
            'form': form,
            'posts': posts
        }

        return render(request, 'posts/view_publications.html', context)

    def post(self, request, *args, **kwargs):
        posting_permission = UserProfile.objects.get(pk=request.user.pk).posting_permission
        form = ResearchPublicationForm(request.POST, request.FILES)
        if form.is_valid():
            if posting_permission:
                new_post = form.save(commit=False)
                new_post.publisher = request.user
                new_post.save()
                form = ResearchPublicationForm() # Clearing the form after submission
            else:
                return render(request, 'posts/no_permission.html')

        return redirect('view-publications')


class PublicationsEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ResearchPublicationList
    fields = ['name']
    template_name = 'posts/publications_edit.html'

    def get_success_url(self):
        return reverse_lazy('view-publications')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class PublicationsDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ResearchPublicationList
    template_name = 'posts/publications_delete.html'
    success_url = reverse_lazy('view-publications')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class NewsView(View):
    def get(self, request, *args, **kwargs):
        form = NewsForm
        posts = News.objects.all().order_by('-publish_date')
        context = {
            'form': form,
            'posts': posts
        }

        return render(request, 'posts/view_news.html', context)

    def post(self, request, *args, **kwargs):
        posting_permission = UserProfile.objects.get(pk=request.user.pk).posting_permission
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            if posting_permission:
                new_post = form.save(commit=False)
                new_post.publisher = request.user
                new_post.save()
                form = NewsForm() # Clearing the form after submission
            else:
                return render(request, 'posts/no_permission.html')

        return redirect('view-news')



class NewsEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title','body']
    template_name = 'posts/news_edit.html'

    def get_success_url(self):
        return reverse_lazy('view-news')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class NewsDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'posts/news_delete.html'
    success_url = reverse_lazy('view-news')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        search_list = Post.objects.filter(body__contains=query)

        context = {
            'search_list': search_list
        }

        return render(request, 'posts/search.html', context)
