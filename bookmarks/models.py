from django.db import models

# Create your models here.


class Bookmark(models.Model):

    title = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
