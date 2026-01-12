from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=False)
    author = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
