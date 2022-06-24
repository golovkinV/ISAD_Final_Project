from datetime import date
from django.db import models


# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class News(models.Model):
    title = models.TextField()
    summary = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(default=date.today())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
