from django.db import models


class User(models.Model):
    username = models.CharField('Name', max_length=10, null=True)


class Discussion(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    like = models.PositiveIntegerField("Like", default=0, editable=False)
    class Meta:
        verbose_name_plural = 'Discussion'


class LikeNum(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = 'user'
