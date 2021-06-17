from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about-us', AboutUs.as_view(), name='about_us'),
    path('contact-us', ContactUs.as_view(), name='contact_us'),
    path('research-team', ResearchTeam.as_view(), name='research_team'),
]
