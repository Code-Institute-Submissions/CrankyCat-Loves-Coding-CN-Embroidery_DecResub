from django.db import models
# from django.contrib.auth.models import User


class Event(models.Model):
    
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )
    title = models.CharField(max_length=70, null=True)
    body = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True)
    abstract = models.CharField(
        max_length=54, blank=True, null=True,
        help_text="get the first 54 text",
    ) 
    views = models.PositiveIntegerField(default=0, null=True) 
    likes = models.PositiveIntegerField(default=0, null=True)
    topped = models.BooleanField(default=False, null=True) 

    def __str__(self):
        return self.title    
    
    class Meta:
        ordering = ['-created_time']


# class AddComment(models.Model):

#     author = models.ForeignKey(
#         User,
#         null=True,
#         on_delete=models.CASCADE
#     )
#     slug = models.SlugField(max_length=200, unique=True, null=True)
#     content = models.TextField(null=True,)
#     created_on = models.DateTimeField(auto_now_add=True, null=True)
#     likes = models.ManyToManyField(
#         User, blank=True
#     )

#     class Meta:
#         ordering = ["-created_on"] 

#     def __str__(self):
#         return self.author