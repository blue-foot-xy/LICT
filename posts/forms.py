# FOR HELP: https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html
from django import forms
from pagedown.widgets import PagedownWidget

from .models import *

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = [ 'title', 'body']
