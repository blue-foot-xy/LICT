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


class StatusViewOngoing(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        posts = Status.objects.all().order_by('-publish_date')
        context = {
            'posts': posts
        }

        return render(request, 'project_management/status_ongoing.html', context)


class StatusViewCompleted(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        posts = Status.objects.all().order_by('-publish_date')
        context = {
            'posts': posts
        }

        return render(request, 'project_management/status_completed.html', context)




class StatusDetail(View):
    def get(self, request, pk, *args, **kwargs):
        post = Status.objects.get(pk=pk)

        context = {
            'post': post,
        }

        return render(request, 'project_management/status_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Status.objects.get(pk=pk)
        if UserProfile.objects.get(pk=request.user.pk).project_management_permission:
            if  'ongoing' in post.state_of_project:
                post.state_of_project = 'completed'
            else:
                post.state_of_project = 'ongoing'
            post.save()
        else:
            return render(request, 'posts/no_permission.html')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class StatusCreate(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        context = {
            'form': form,
        }

        return render(request, 'project_management/status_create.html', context)

    def post(self, request, *args, **kwargs):
        project_management_permission = UserProfile.objects.get(pk=request.user.pk).project_management_permission
        form = StatusForm(request.POST, request.FILES)
        if form.is_valid():
            if project_management_permission:
                new_post = form.save(commit=False)
                new_post.publisher = request.user
                new_post.save()
                form = StatusForm() # Clearing the form after submission
            else:
                return render(request, 'posts/no_permission.html')

        return redirect('status')


class StatusEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Status
    fields = ['title', 'introduction', 'background', 'scope_of_work', 'objective', 'project_duration', 'principle_investigator', 'co_investigator', 'team_members', 'advisors', 'international_experts', 'phd_research_scholars', 'funding', 'estimated_completion_date', 'other_description']
    template_name = 'project_management/status_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('status-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher


class StatusDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Status
    template_name = 'project_management/status_delete.html'
    success_url = reverse_lazy('status')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.publisher
