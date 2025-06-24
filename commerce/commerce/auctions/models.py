from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} {self.name}"

class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.id} {self.title}, {self.description} begins at {self.starting_bid}"
    
class Comment(models.Model):
    comment = models.TextField()
    time_stamp = models.DateTimeField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")