from django.db import models


# Create your models here.
class Tweet(models.Model):
    tweet = models.TextField(max_length=280)
