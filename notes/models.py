from django.db import models

from uuid import uuid4


class Note(models.Model):
    # TODO: Add author

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # TODO: Maybe add categories?


class Bookmark(models.Model):

    title = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
