from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        contents = HomePageMessages.objects.get(pk=1)
        carousel_images = HomePageCarouselImage.objects.all()

        context = {
            'contents': contents,
            'carousel_images': carousel_images
        }
        return render(request, 'other_pages/home.html', context)


class AboutUs(View):
    def get(self, request, *args, **kwargs):
        visions = Vision.objects.all()
        missions = Mission.objects.all()
        goals = Goal.objects.all()
        tasks = Task.objects.all()

        context = {
            'visions': visions,
            'missions': missions,
            'goals': goals,
            'tasks': tasks
        }

        return render(request, 'other_pages/about_us.html', context)


class ContactUs(View):
    def get(self, request, *args, **kwargs):
        contacts = Contact.objects.get(pk=1)

        context = {
            'contacts': contacts,
        }

        return render(request, 'other_pages/contact_us.html', context)


class ResearchTeam(View):
    def get(self, request, *args, **kwargs):
        research_team = ResearchTeamMember.objects.all()

        context = {
            'research_team': research_team,
        }

        return render(request, 'other_pages/research_team.html', context)


class CVUpload(View):
    def get(self, request, *args, **kwargs):
        vacancy_announcements = VacancyAnnouncement.objects.all()
        form = CVUploadForm()
        context = {
            'vacancy_announcements' : vacancy_announcements,
            'form': form,
        }
        return render(request, 'posts/vacancy.html', context)

    def post(self, request, *args, **kwargs):
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = CVUploadForm()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
