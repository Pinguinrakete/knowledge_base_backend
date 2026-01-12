from django.db import models

class Data(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    text = models.TextField(blank=False)
    author = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
