from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    """store events"""

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=70, null=True)
    abstract = models.CharField(
        max_length=100, blank=True, null=True,
        help_text="Write a post excerpt within 200 characters",
    )
    body = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True)
    views = models.PositiveIntegerField(default=0, null=True)
    likes = models.PositiveIntegerField(default=0, null=True)
    topped = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_time']


class Comment(models.Model):
    """event comments"""

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["created_time", ]

    def __str__(self):
        return self.body[:20]

