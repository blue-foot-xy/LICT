from django import forms

from markdownx.fields import MarkdownxFormField

from .models import *

class StatusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['estimated_completion_date'].label = "Estimated Completion Date (YYYY-MM-DD)"
        self.fields['introduction'].label = "Introduction (You can drag & drop images into this field)"

    introduction = MarkdownxFormField()
    state_of_project = forms.CharField(label='State of the project', widget=forms.Select(choices=[('ongoing', 'Ongoing'),
                                                                                               ('completed', 'Completed')]))

    class Meta:
        model = Status
        fields = ['title', 'state_of_project', 'introduction', 'objective', 'project_duration', 'background', 'scope_of_work',  'principle_investigator', 'co_investigator', 'team_members', 'advisors', 'international_experts', 'phd_research_scholars', 'funding', 'estimated_completion_date', 'other_description']
