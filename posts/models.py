from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:300] + " ...."

    def pretty_date(self):
        return self.publish_date.strftime('%b %e %Y')
