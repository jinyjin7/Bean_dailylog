from django.db import models
from user.models import User
# Create your models here.


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=15)
    content = models.CharField(max_length=150)
    article_img = models.ImageField(
        blank=True, null=True, upload_to="media/photo/%Y/%m/%d", default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    diary = models.ForeignKey(
        Diary, related_name="comment", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Feed_like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    feed = models.ForeignKey(Diary, on_delete=models.CASCADE, null=True)


class Boookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Diary = models.ForeignKey(
        Diary, related_name="comments", on_delete=models.CASCADE)
