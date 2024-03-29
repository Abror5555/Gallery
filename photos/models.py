from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=155, null=False, blank=False)

    def __str__(self):
        return self.name




class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description
