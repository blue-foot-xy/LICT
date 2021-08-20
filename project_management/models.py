from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
import markdown
md = markdown.Markdown()

class Status(models.Model):
    title = models.CharField(max_length=2000)
    state_of_project = models.CharField(max_length=10, default='ongoing')
    introduction = models.TextField(blank=True)
    background = models.TextField(blank=True)
    scope_of_work = models.TextField(blank=True)
    objective = models.CharField(max_length=2000, blank=True)
    project_duration = models.CharField(max_length=100, blank=True)
    principle_investigator = models.CharField(max_length=500, blank=True)
    co_investigator = models.CharField(max_length=500, blank=True)
    team_members = models.TextField(blank=True)
    advisors = models.TextField(blank=True)
    international_experts = models.TextField(blank=True)
    phd_research_scholars = models.TextField(blank=True)
    funding = models.CharField(max_length=100, blank=True)
    estimated_completion_date =  models.CharField(max_length=100, blank=True)
    other_description = models.TextField(blank=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def introduction_html(self):
        return md.convert(self.introduction)
