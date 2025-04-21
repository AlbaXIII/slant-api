from django.db import models
from django.contrib.auth.models import User
from articles.models import Article
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, related_name='ratings', on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        default=5, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'article']

    def __str__(self):
        return f'{self.owner} {self.article}'
