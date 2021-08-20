from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import markdown
md = markdown.Markdown()


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def summary(self):
        return md.convert(self.body[:300])

    def pretty_date(self):
        return self.publish_date.strftime('%b %e %Y')

    def body_html(self):
        return md.convert(self.body)


class ResearchDomains(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def pretty_date(self):
        return self.publish_date.strftime('%b %e %Y')

    def body_html(self):
        return md.convert(self.body)


class ResearchPublicationList(models.Model):
    name = models.CharField(max_length=2000)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def pretty_date(self):
        return self.publish_date.strftime('%b %e %Y')

    def body_html(self):
        return md.convert(self.body)
