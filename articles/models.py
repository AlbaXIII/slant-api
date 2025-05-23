from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    subject_field_choices = [
        ('news', 'News'),
        ('sport', 'Sport'),
        ('culture', 'Culture'),
        ('opinion', 'Opinion'),
        ('lifestyle', 'Lifestyle'),
        ('reviews', 'Reviews'),
        ('travel', 'Travel'),
        ('other', 'Other'),
    ]

    publisher_field_choices = [
        ('original content', 'Original Content'),
        ('the guardian', 'The Guardian'),
        ('daily mail', 'Daily Mail'),
        ('the independant', 'The Independant'),
        ('daily telegraph', 'Daily Telegraph'),
        ('daily express', 'Daily Express'),
        ('the sun', 'The Sun'),
        ('financial times', 'Financial Times'),
        ('metro', 'Metro'),
        ('the times', 'The Times'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    publisher = models.CharField(max_length=32,
                                 choices=publisher_field_choices,
                                 default='original content')
    subject = models.CharField(max_length=32,
                               choices=subject_field_choices, default='news')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, default="link")
    image = models.ImageField(
        upload_to='images/', default='../slant-default-image_ff67lu',
        blank=True
    )
    body = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
