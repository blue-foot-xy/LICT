from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import UserProfile
from posts.models import Post


# Create your views here.
class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(publisher=user).order_by('-publish_date')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
        }

        return render(request, 'user/profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['name', 'bio', 'designation', 'profile_pic']
    template_name = 'user/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class EditPermissionView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['posting_permission', 'project_management_permission']
    template_name = 'user/give_permission.html'

    def get_success_url(self):
        return reverse_lazy('manage-permission')

    def test_func(self):
        return self.request.user.is_superuser


class ManagePermissionView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        profiles = UserProfile.objects.all()
        context = {
            'profiles': profiles,
        }
        return render(request, 'user/manage_permissions.html', context)

    def test_func(self):
        return self.request.user.is_superuser
