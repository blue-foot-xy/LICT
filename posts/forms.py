# FOR HELP: https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html
from django import forms

from markdownx.fields import MarkdownxFormField

from .models import *

class PostForm(forms.ModelForm):
    body = MarkdownxFormField()

    class Meta:
        model = Post
        fields = [ 'title', 'body']


class ResearchDomainForm(forms.ModelForm):
    body = MarkdownxFormField()

    class Meta:
        model = ResearchDomains
        fields = [ 'title', 'body']


class ResearchPublicationForm(forms.ModelForm):
    class Meta:
        model = ResearchPublicationList
        fields = [ 'name']

class NewsForm(forms.ModelForm):
    body = MarkdownxFormField()

    class Meta:
        model = News
        fields = [ 'title', 'body']
