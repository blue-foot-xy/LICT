from django import forms

from markdownx.fields import MarkdownxFormField

from .models import *

class StatusForm(forms.ModelForm):
    introduction = MarkdownxFormField()
    state_of_project = forms.CharField(label='State of the project', widget=forms.Select(choices=[('ongoing', 'Ongoing'),
                                                                                               ('completed', 'Completed')]))

    class Meta:
        model = Status
        fields = ['title', 'state_of_project', 'introduction', 'objective', 'project_duration', 'background', 'scope_of_work',  'principle_investigator', 'co_investigator', 'team_members', 'advisors', 'international_experts', 'phd_research_scholars', 'funding', 'estimated_completion_date', 'other_description']
