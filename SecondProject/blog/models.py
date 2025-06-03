from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        app_label = 'blog_db'

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'blog_db'