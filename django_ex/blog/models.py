from django.db import models
from django.shortcuts import render
# Create your models here.
from django.db import models


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    brief_content = models.TextField()
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
