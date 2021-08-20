from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Post)
admin.site.register(ResearchDomains)
admin.site.register(ResearchPublicationList)
admin.site.register(News)
