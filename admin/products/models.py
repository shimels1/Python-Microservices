from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    link = models.PositiveIntegerField(max_length=200)

class User(models.Model):
    pass
