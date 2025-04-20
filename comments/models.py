from django.db import models
from django.contrib.auth.models import User
from articles.models import Article


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=500)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.body
