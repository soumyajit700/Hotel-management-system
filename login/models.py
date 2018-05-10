from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Book(models.Model):
    From = models.CharField(max_length=40)
    To = models.CharField(max_length=40)
    Type = models.CharField(max_length=40)
    requirements = models.CharField(max_length=40)
    adults = models.CharField(max_length=40)
    children = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    phone = models.CharField(max_length= 40)
