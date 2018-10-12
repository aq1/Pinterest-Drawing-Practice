from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    pinterest_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
