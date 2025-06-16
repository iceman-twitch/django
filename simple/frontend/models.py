from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)

class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    video = models.CharField(max_length=200)
    
class Url(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    banner = models.CharField(max_length=200)
    