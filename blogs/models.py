from django.db import models

# Create your models here.
from django.db import models
from database.models import CustomUser

class Blog(models.Model):
    body = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)