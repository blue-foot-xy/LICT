from django.db import models

######################## HOME PAGE ########################
class HomePageMessages(models.Model):
    deans_message = models.TextField()
    deans_photo =  models.ImageField(
                        upload_to='home-pg-photos/',
                        blank=True,
                        null=True)
    chairmans_message = models.TextField()
    chairmans_photo =  models.ImageField(
                        upload_to='home-pg-photos/',
                        blank=True,
                        null=True)

    def deans_message_summary(self):
        return self.deans_message[:300] + '...'

    def chairmans_message_summary(self):
        return self.chairmans_message[:300] + '...'

class HomePageCarouselImage(models.Model):
    image =  models.ImageField(
                        upload_to='home-pg-photos/',
                        blank=True,
                        null=True)

####################### ABOUT US PAGE #######################
class Vision(models.Model):
    vision = models.CharField(max_length=200)

class Mission(models.Model):
    mission = models.CharField(max_length=200)

class Goal(models.Model):
    goal = models.CharField(max_length=200)

class Task(models.Model):
    task = models.CharField(max_length=200)


####################### CONTACT US PAGE #######################
class Contact(models.Model):
    organization_name = models.CharField(max_length=200)
    college_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


######################### VACANCY PAGE #########################
class VacancyAnnouncement(models.Model):
    title =  models.CharField(max_length=200)
    description = models.TextField()

class CVUpload(models.Model):
    cv_pdf = models.FileField(upload_to='cv/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


###################### RESEARCH TEAM PAGE ######################
class ResearchTeamMember(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(
                upload_to='rnd-team-photos/',
                blank=True,
                null=True)
    post = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone_no = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=200, blank=True)
    remarks = models.TextField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
