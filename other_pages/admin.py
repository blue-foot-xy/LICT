from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(ResearchTeamMember)
admin.site.register(Contact)
admin.site.register(Vision)
admin.site.register(Mission)
admin.site.register(Goal)
admin.site.register(Task)
admin.site.register(HomePageMessages)
admin.site.register(HomePageCarouselImage)
