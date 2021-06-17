from django import forms
from .models import *

class CVUploadForm(forms.ModelForm):
    class Meta:
        model = CVUpload
        fields = ('cv_pdf', )
