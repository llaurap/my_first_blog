from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=300)
    year = models.PositiveIntegerField(default=2020)
    month = models.PositiveIntegerField(default=1)
    month_to_display = models.CharField(max_length=60, default="")
    description = models.CharField(blank=True, max_length=120)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
